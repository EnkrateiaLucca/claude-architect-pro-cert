# Exercise 2: Caching and Context Strategy

**Lesson:** 02 · **Time:** 15 minutes · **Format:** run a script, then a design drill

## Part 1: Watch caching work and break (runnable)

```bash
export ANTHROPIC_API_KEY=...
uv run exercises/scripts/prompt_caching.py
```

The script sends three questions against a ~2,500-token policy prefix in three layouts. Read the `cache_write` / `cache_read` columns:

1. **Static prefix with a breakpoint.** The first call writes the cache; the next two read it.
2. **Timestamp before the policy.** Every call writes. The cache never hits, and you pay the write premium each time.
3. **Timestamp after the cached block.** Reads return.

**What to look for:** one misplaced dynamic value turns a cost saving into a cost increase. This is the pattern behind official Sample 2 and practice question Q40.

## Part 2: Design the context strategy

A legal-research assistant serves 300 lawyers. Each request includes:

- a 6,000-token firm style guide (changes quarterly)
- 25 tool definitions, of which a typical request uses 3
- the matter's documents, 20k–400k tokens per matter
- the lawyer's question
- the current date

Long research sessions run 80+ turns and start forgetting instructions the lawyer gave early.

Decide:

1. Prompt order and cache breakpoints.
2. Monolithic or progressive for the tools.
3. Long context or RAG for the matter documents.
4. How to keep long sessions on track.
5. Which model and effort to start with, and how you'd decide to change.

<details><summary>Reference answer</summary>

1. **Order:** tools → system (style guide) → matter documents → conversation → date and question last. Breakpoints after the tools/style guide and after the matter documents. Matter documents are stable within a matter, so a 1-hour TTL can pay off for long sessions.
2. **Tools:** defer rarely used tools behind tool search (it preserves the cache), or route to scoped sub-agents. Keep the 3–5 common tools loaded.
3. **Documents:** matters under ~200k tokens go in context with caching. Larger matters get hybrid RAG (contextual chunking, BM25 + embeddings, reranking) with citations.
4. **Long sessions:** a structured "matter facts and instructions" block that persists, context editing to clear stale tool results, compaction for old turns, and a memory file for durable facts.
5. **Model and effort:** start capability-first (a large model at default effort) because legal errors are costly, then test lower effort and a smaller model on the eval set. Switch only if quality holds and cost per completed task falls.

</details>
