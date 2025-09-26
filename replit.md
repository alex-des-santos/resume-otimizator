# AI Career Assistant - Resume Optimizer

## Overview
This is a static HTML-based AI-powered career assistant application that helps users:
- Optimize resumes for specific job postings using Google Gemini AI
- Generate cover letters, LinkedIn optimizations, and interview questions
- Create professional pitches and follow-up emails
- Export optimized resumes as PDFs

## Project Architecture
- **Type**: Frontend-only static web application
- **Language**: HTML5, CSS3, JavaScript (ES6+)
- **Dependencies**: All loaded via CDN (Tailwind CSS, pdf.js, jsPDF, marked.js)
- **AI Integration**: Google Gemini API for content generation
- **Hosting**: Simple HTTP server serving static files

## Current Setup
- **Development Server**: Python HTTP server on port 5000
- **Workflow**: "Frontend Server" serving on 0.0.0.0:5000
- **Deployment**: Configured for autoscale deployment target
- **Status**: ✅ Fully functional and ready to use

## Files Structure
- `index.html` - Main application interface
- `test.html` - Basic dependency testing page
- `test-complete.html` - Comprehensive functionality testing
- `README.md` - Project documentation
- `LICENSE` - MIT license
- `SECURITY.md` - Security guidelines
- `FIXES.md` - Known fixes and improvements

## Features
- Resume optimization for ATS compatibility
- Job description extraction from LinkedIn URLs
- PDF upload and text parsing
- Multi-language support (Portuguese/English)
- Real-time markdown preview
- Security-focused with CSP headers
- Mobile-responsive design

## Dependencies (CDN)
- Tailwind CSS 2.2.19
- pdf.js 2.11.338
- jsPDF 2.5.1
- marked.js 4.3.0
- Google Fonts (Inter)

## Recent Changes
- 2025-09-26: Initial Replit environment setup
- Set up Python HTTP server for static file serving
- Configured deployment for production autoscale
- Verified all CDN dependencies working correctly
- Tested application functionality successfully

## User Preferences
- Prefers Portuguese language interface
- Uses Google Gemini AI for content generation
- Security-conscious with proper CSP headers
- Clean, professional UI with Tailwind CSS