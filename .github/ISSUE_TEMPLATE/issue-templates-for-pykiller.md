---
name: Issue Templates for PYKILLER
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

### **Issue Templates for PYKILLER**

Issue templates help streamline the process of reporting bugs, suggesting features, or requesting support for the **PYKILLER** project. By providing a clear and structured way to report issues, we ensure that maintainers can quickly identify and address concerns.

Below are example **issue templates** for various use cases, such as bug reports, feature requests, and support inquiries.

---

### **1. Bug Report Template**

When creating a bug report, please fill out the sections below. Providing all relevant information will help us resolve the issue more efficiently.

```markdown
## Bug Report

**Description:**
A clear and concise description of the issue.

**Steps to Reproduce:**
1. Step 1
2. Step 2
3. Step 3

**Expected Behavior:**
A description of what you expected to happen.

**Actual Behavior:**
A description of what actually happened.

**Error Logs (if applicable):**
Include any error logs or stack traces related to the bug.
```

#### **Example Bug Report**

```markdown
## Bug Report

**Description:**
When running PYKILLER on a fresh system, it crashes after a few minutes, consuming all available memory.

**Steps to Reproduce:**
1. Clone the repository and set up the environment.
2. Run the PYKILLER script with default settings.
3. Observe the system behavior after 5-10 minutes of execution.

**Expected Behavior:**
The script should complete its execution without crashing the system.

**Actual Behavior:**
The system becomes unresponsive, and a "Memory Overflow" error is triggered.

**Error Logs:**
```
```
MemoryError: Unable to allocate 10.0 GB for an array.
```
```

---

### **2. Feature Request Template**

If you have an idea for a new feature or improvement, please use the following template to clearly explain your suggestion.

```markdown
## Feature Request

**Feature Description:**
A clear and concise description of the feature you’d like to see added or improved.

**Why is this Feature Needed:**
Explain why this feature would benefit the project or its users.

**Additional Context (optional):**
Provide any additional context, mockups, or examples that can help maintainers understand the feature.
```

#### **Example Feature Request**

```markdown
## Feature Request

**Feature Description:**
Introduce a "safe mode" where PYKILLER limits resource usage (memory/CPU) and allows users to test the tool in non-critical environments.

**Why is this Feature Needed:**
The current version of PYKILLER can consume all available system resources, making it dangerous for systems without proper safeguards. A safe mode would allow more controlled testing.

**Additional Context:**
A configuration flag `--safe-mode` could be added to limit the CPU and memory consumption. Users can set max values for resource consumption to avoid crashes.
```

---

### **3. Support Request Template**

If you are encountering issues while using PYKILLER and need support, please provide the following information so we can assist you better.

```markdown
## Support Request

**Description of the Issue:**
A brief description of the problem or question you have.

**Steps to Reproduce:**
1. Step 1
2. Step 2
3. Step 3

**Expected Outcome:**
What you expected to happen.

**Actual Outcome:**
What actually happened (include any error messages or logs if possible).

**Environment Details:**
- OS Version: [e.g., Ubuntu 20.04]
- Python Version: [e.g., Python 3.8]
- Pygame Version: [e.g., Pygame 2.0.1]
- Any other relevant software or versions
```

#### **Example Support Request**

```markdown
## Support Request

**Description of the Issue:**
I am unable to run PYKILLER on my system, and it crashes with a "Segmentation Fault" error.

**Steps to Reproduce:**
1. Clone the repository.
2. Install all required dependencies.
3. Run `python pykiller.py` on a Ubuntu 20.04 system.

**Expected Outcome:**
PYKILLER should run without errors.

**Actual Outcome:**
I get a "Segmentation Fault" after running the script for a few seconds.

**Environment Details:**
- OS Version: Ubuntu 20.04
- Python Version: Python 3.8
- Pygame Version: Pygame 2.0.1
```

---

### **4. Documentation Issue Template**

If you spot any errors or issues in the project's documentation, please use the following template to report them.

```markdown
## Documentation Issue

**Page or Section with Issue:**
Provide the name or URL of the page, or section title where the issue appears.

**Issue Description:**
Describe the error or problem with the documentation (e.g., outdated information, missing steps).

**Suggested Fix:**
Provide any suggestions or corrections to improve the documentation.
```

#### **Example Documentation Issue**

```markdown
## Documentation Issue

**Page or Section with Issue:**
README.md, "Installation" section

**Issue Description:**
The instructions for installing dependencies are outdated, and the command `pip install pygame` doesn’t work for Python 3.8.

**Suggested Fix:**
Update the installation instructions to reflect the need to use `python3 -m pip install pygame` for Python 3.8.
```

---

### **5. Code of Conduct Violation Template**

If you witness or experience behavior that violates the project’s Code of Conduct, please report it using this template.

```markdown
## Code of Conduct Violation

**Description of the Incident:**
A brief description of the incident, including the individual(s) involved, if known.

**Date and Time of Incident:**
Provide the date and time of the incident.

**Location of Incident:**
Where did the incident occur? (e.g., GitHub Issues, PR comments, Discord)

**Evidence (if applicable):**
Any links, screenshots, or other evidence to support the report.

**Suggested Action:**
What action do you believe should be taken (e.g., warning, removal from project)?
```

#### **Example Code of Conduct Violation Report**

```markdown
## Code of Conduct Violation

**Description of the Incident:**
A user posted offensive comments in the "Installation Issues" thread and made derogatory remarks about another contributor's code style.

**Date and Time of Incident:**
January 10, 2025, 2:30 PM UTC

**Location of Incident:**
GitHub Issues – "Installation Issues" thread

**Evidence (if applicable):**
[Link to the issue thread](https://github.com/pykiller/pykiller/issues/15)

**Suggested Action:**
The user should be given a warning or temporarily banned from commenting on the repository.
```

---

### **Conclusion**

By using these templates, contributors and maintainers can quickly and efficiently address issues, requests, and concerns related to **PYKILLER**. Please ensure that you fill out the template fully and provide as much detail as possible to help us address your issue in a timely manner.

Feel free to adapt or expand these templates as necessary based on your specific needs.
