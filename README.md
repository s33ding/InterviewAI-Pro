# InterviewAI-Pro

InterviewAI-Pro is an AI-powered technical interview prep platform that transforms educational content into interactive quizzes and questions.

## Architecture Flow

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Step 0        │    │   Step 1        │    │   Step 2        │    │   Step 3        │
│   Setup         │───▶│   Extract       │───▶│   Generate      │───▶│   Create Quiz   │
│                 │    │                 │    │                 │    │                 │
│ • User inputs   │    │ • Read files    │    │ • AI questions  │    │ • Python quiz   │
│ • Create config │    │ • Clean output  │    │ • Clean format  │    │ • Interactive   │
│ • input.json    │    │ • Save content  │    │ • Save markdown │    │ • Bedrock AI    │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │                       │
         ▼                       ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   input.json    │    │ topic_extracted │    │ topic_questions │    │   topic.py      │
│                 │    │   _content.txt  │    │     .md         │    │                 │
│ • topic_name    │    │                 │    │                 │    │ • Full quiz     │
│ • source_folder │    │ • Clean content │    │ • Discussion Q  │    │ • AI feedback   │
│ • num_questions │    │ • Educational   │    │ • Understanding │    │ • Interactive   │
│ • output_dir    │    │   summary       │    │ • Multiple choice│    │   experience    │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Pipeline Steps

### Step 0: Setup Configuration
- Interactive prompts for user inputs
- Creates `input.json` with configuration
- Defines topic, source folder, question count, output directory

### Step 1: Content Extraction (ETL - Extract & Transform)
- Reads all files from source folder
- Uses Q chat AI to extract and summarize key concepts
- Cleans ANSI codes and status messages from output
- Saves clean educational content to `{topic}_extracted_content.txt`
- Updates `input.json` with `extracted_content_path`

### Step 2: Question Generation (ETL - Transform)
- Reads extracted content from step 1
- Uses Q chat AI to generate three types of questions:
  - Discussion questions with follow-ups
  - Understanding questions with answers
  - Multiple choice questions with explanations
- Cleans output formatting
- Saves to `{topic}_questions.md`
- Updates `input.json` with `questions_path`

### Step 3: Quiz Creation (ETL - Load)
- Reads questions from step 2
- Uses Q chat AI to create interactive Python quiz
- Integrates with AWS Bedrock for AI-powered feedback
- Creates executable quiz file `{topic}.py`

## Usage

### Run Complete Pipeline
```bash
python main.py
```

### Run Specific Steps
```bash
python main.py 0        # Setup only
python main.py 1 2      # Extract and generate questions
python main.py 3        # Create quiz only
```

### Testing
```bash
# Test individual steps
cd test
python test_step0.py    # Validate input.json
pytest test_step1.py -v # Test extraction
pytest test_step2.py -v # Test question generation

# Quick test with sample data
python test_run.py
```

## File Structure
```
InterviewAI-Pro/
├── main.py                 # Pipeline orchestrator
├── input.json             # Configuration (auto-generated)
├── steps/                 # Pipeline steps
│   ├── step0_setup.py
│   ├── step1_extract.py
│   ├── step2_generate_questions.py
│   └── step3_create_quiz.py
├── test/                  # Test files and sample data
│   ├── sample_content/
│   ├── test_input.json
│   └── test_step*.py
└── {output_dir}/          # Generated content
    ├── {topic}_extracted_content.txt
    ├── {topic}_questions.md
    └── {topic}.py
```

## Development Phases

### Phase 1: Shell-based POC (Current)
- Command-line interface for personal use
- Local file storage for questions and progress
- Direct API calls to AI services (Q chat, Bedrock)
- Minimal dependencies for rapid prototyping

### Phase 2: AWS Deployment (Planned)
- Serverless architecture using Lambda, S3, Cognito, Lex, and Bedrock
- Web interface for sharing and collaboration
- Scalable, secure multi-user platform

## Features
- **Multi-format Support**: Processes any file type (markdown, code, text, etc.)
- **AI-Powered Extraction**: Uses Q chat for intelligent content summarization
- **Three Question Types**: Discussion, understanding, and multiple choice
- **Clean Output**: Removes formatting artifacts and status messages
- **Interactive Quizzes**: Python-based quizzes with AI feedback
- **Modular Pipeline**: Run individual steps or complete workflow
- **Test Coverage**: Comprehensive testing for each pipeline step
