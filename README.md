# Chloe TV Content Repository

This repository serves as the central hub for all content and visual assets related to Chloe AI TV, a 24-hour AI-driven stream. The content is organized to support a continuous cycle between a noon educational pulse and a midnight adult pulse.

## Repository Structure

*   **`scripts/`**: Contains all generated and curated scripts for AI talk shows, animated segments, human reflection sessions, and any other narrative content.
*   **`visuals/`**: Stores visual assets, including animated character models, background art, scene compositions, and any other graphical elements used in the stream. Visuals can be generated on-device or remotely and are synced here.
*   **`audio/`**: Holds audio files such as voiceovers, sound effects, background music, and any other auditory components.
*   **`submissions/`**: This directory is designated for open submissions from external sources. At the end of each 12-hour cycle, AI will process and merge content from this directory into the next storyline.
*   **`metadata/`**: Contains metadata files, scheduling information, content tags, and other administrative data crucial for the autonomous operation and content rotation of Chloe TV.

## Content Contribution and Organization

All content should be organized logically within these directories. Filenaming conventions and sub-directory structures within each main directory will be established as content generation progresses to ensure consistency and ease of retrieval by the autonomous system.

## Autonomous Operation

Gemini autonomously manages content rotation, loop scheduling, and viewer interaction flow. Submissions are integrated to evolve segments across time, maintaining the noon/midnight rhythm.
