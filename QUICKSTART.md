# Quick Start Guide

Get started with the Python and Deep Learning book in 5 minutes!

## Step 1: Prerequisites

Make sure you have:
- Python 3.8 or higher installed
- pip (Python package manager)
- Git (for cloning the repository)

To check your Python version:
```bash
python --version
```

## Step 2: Clone the Repository

```bash
git clone https://github.com/aprose/Python-Intro-Book.git
cd Python-Intro-Book
```

## Step 3: Set Up Your Environment

### Option A: Install Dependencies Globally
```bash
pip install -r requirements.txt
```

### Option B: Use a Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Step 4: Start Learning

### For Interactive Learning (Recommended)
```bash
jupyter notebook
```

This will open Jupyter in your browser. Navigate to:
- `chapters/01-python-basics/` to start with Python fundamentals
- `chapters/05-deep-learning-basics/` if you already know Python

### For Script-Based Learning
```bash
# Run example code
cd examples
python simple_neural_network.py

# Run exercise solutions
cd ../exercises/solutions
python chapter1_solutions.py
```

## Step 5: Follow the Learning Path

1. **Complete Beginner**: Start with Chapter 1 (Python Basics)
2. **Some Python Experience**: Start with Chapter 2 or 3
3. **Ready for Deep Learning**: Jump to Chapter 5
4. **Advanced Learner**: Explore Chapters 6 and 7

## Recommended Learning Schedule

### Week 1-2: Python Fundamentals
- Chapter 1: Python Basics
- Chapter 2: Python Intermediate
- Complete exercises

### Week 3-4: Advanced Python & Data Science
- Chapter 3: Python Advanced
- Chapter 4: Data Science Introduction
- Build small projects

### Week 5-6: Deep Learning Foundations
- Chapter 5: Deep Learning Basics
- Chapter 6: Neural Networks
- Implement simple models

### Week 7-8: Advanced Topics
- Chapter 7: Advanced Deep Learning
- Final projects
- Explore additional resources

## Tips for Success

1. **Practice Daily**: Even 30 minutes a day is better than cramming
2. **Type the Code**: Don't just read - type and run the examples
3. **Complete Exercises**: Practice is key to mastery
4. **Build Projects**: Apply what you learn to real problems
5. **Join Communities**: Connect with other learners online

## Troubleshooting

### Import Errors
If you get `ModuleNotFoundError`, make sure you've installed all dependencies:
```bash
pip install -r requirements.txt
```

### Jupyter Not Found
Install Jupyter:
```bash
pip install jupyter notebook
```

### Python Version Issues
This book requires Python 3.8+. Update if needed:
- Windows: Download from [python.org](https://www.python.org/downloads/)
- macOS: Use Homebrew: `brew install python@3.11`
- Linux: Use your package manager: `sudo apt install python3.11`

## Need Help?

- Check the [README.md](README.md) for detailed information
- Review [CONTRIBUTING.md](CONTRIBUTING.md) to add content
- Open an issue on GitHub for questions

Happy Learning! 🚀
