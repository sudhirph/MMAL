# Multi-Model AI Hub

A modern, responsive frontend for interacting with various AI model providers through a unified interface.

## Project Overview

This project provides a sleek interface to interact with multiple AI model providers including OpenAI, Anthropic, Gemini, and Ollama. Features include:

- Tabbed interface with provider logos
- Model selection based on provider
- Prompt input and response display
- Light/dark mode toggle
- Responsive design for all devices

## How to Download and Use

## Front end code

### Option 1: Clone the Repository

```bash
git clone [repository-url]
cd MMAL-FE
npm install
npm run dev
```

### Option 2: Download as ZIP

1. Download this project as a ZIP file
2. Extract to your desired location
3. Open a terminal in the extracted folder
4. Run `npm install` followed by `npm run dev`



## Back end code

### Option 1: Clone the Repository

```bash
git clone [repository-url]
cd MMAL-BE
docker-compose up --build
```

### Option 2: Download as ZIP

1. Download this project as a ZIP file
2. Extract to your desired location
3. Open a terminal in the extracted folder
4. Run `docker-compose up --build` 




Create a `.env` file in the root directory with your API keys:

```
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
# Add other API keys as needed
```

## Customizing the UI

The UI is built with React, Tailwind CSS, and shadcn components. You can customize:

- Colors and themes in `tailwind.config.ts` and `client/src/index.css`
- Component styling in their respective files
- Add new providers by extending the provider tabs component

URL to run your app locally - http://localhost:5000/

Screen shot 

![Screenshot 2025-05-20 at 8 07 43 AM](https://github.com/user-attachments/assets/e5c273fa-c2c8-4706-9620-1e3c3eebcee6)

![Screenshot 2025-05-20 at 8 11 34 AM](https://github.com/user-attachments/assets/7b7aa872-a07c-49d8-87ae-65cc476c62ef)

