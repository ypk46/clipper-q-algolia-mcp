# Clipper: Orchestrating Amazon Q with Algolia MCP for Read-Later Link Management

## Overview

Clipper is a creative CLI agent that leverages Amazon Q’s orchestration capabilities and Algolia’s Model Context Protocol (MCP) to help you save, enrich, and search your read-later links. Designed for the DEV code challenge, Clipper demonstrates how LLMs and MCP tools can be combined to build a personal knowledge manager for URLs.

## How It Works

1. **Custom Amazon Q Profile**

   - A custom profile is created using the Amazon Q CLI.
   - The `instructions.md` file is added as context, guiding Q on how to process URLs, extract content, and interact with Algolia MCP.

2. **Clipping a URL**

   - The agent receives a URL.
   - It uses a custom MCP tool to open and extract the content of the link.
   - Q generates a summary and relevant keywords from the article.
   - The current date is recorded.
   - An entry is added to the Algolia index `clipper` with:
     - Title
     - Summary
     - Keywords
     - Date added (YYYY-MM-DD)
     - URL

3. **Searching Your Links**

   - The agent analyzes your query and converts it into an Algolia search.
   - It retrieves the most relevant entries from the `clipper` index.
   - Results are presented with concise messages and direct URLs.

4. **Fallback Handling**
   - If content extraction fails, the agent offers to save the URL with a title derived from the URL and the current date.

## Key Features

- **LLM-Orchestrated Enrichment:**  
  Amazon Q uses the provided instructions to coordinate MCP tools and enrich each link with summaries and keywords.
- **Algolia MCP Integration:**  
  All entries are indexed in Algolia, enabling fast and flexible search.
- **CLI Simplicity:**  
  The workflow is fully automated via the CLI, requiring minimal user input.
- **Extensible Design:**  
  Easily add new enrichment or search tools by updating the MCP toolset or instructions.

## Usage

1. **Setup Amazon Q CLI**

   Create a profile.

   ```bash
   q chat
   > /profile create [profile-name]
   ```

   Add `instructions.md` as context

   ```bash
   q chat --profile [profile-name]
   > /context add instructions.md
   ```

2. **Clip a Link**
   Run Q using your profile and provide a link.

   ```bash
   q chat --profile [profile-name]
   > Clip this link [url]
   ```

3. **Search Links**
   Run Q using your profile and provide a search query.

   ```bash
   q chat --profile [profile-name]
   > Hey, search for the link about Algolia MCP
   ```
