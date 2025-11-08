## **Task 1 Summary – Git & Environment Setup**

**Objective:**
Set up a clean, reproducible development environment with proper version control, project structure, and continuous integrai wanna add it into gitignotion.

---

### **1. Repository Setup**

* Created a new GitHub repository: `solar-challenge-week0`.
* Cloned the repository locally to your computer.
* Created a branch for Task 1 (e.g., `task0-setup`) to work safely without affecting `main`.

---

### **2. Project Structure**

* Created essential project folders:

```
.github/workflows
src
notebooks
tests
scripts
app
data
dashboard_screenshots
```

* This ensures proper organization for code, notebooks, tests, scripts, app files, and dashboards.

---

### **3. Essential Files**

* Created key files for project setup:

  * `requirements.txt` → for Python dependencies.
  * `.gitignore` → to ignore unnecessary files (like `__pycache__`, `.env`, `data/`).
  * `README.md` → to document project setup and instructions.

---

### **4. Python Environment**

* Created a Python virtual environment:

```powershell
py -m venv venv
```

* Activated the virtual environment:

```powershell
venv\Scripts\activate
```

* Ready to install dependencies inside the isolated environment.

---

### **5. Git Workflow**

* Added and committed changes to the branch:

```powershell
git add .
git commit -m "Completed Task 0 setup"
```

* Pushed the branch to GitHub:

```powershell
git push origin task0-setup
```

* Opened a Pull Request (PR) on GitHub to merge `task0-setup` into `main`.



### **6. Continuous Integration (CI)**

* Created a GitHub Actions workflow file `.github/workflows/ci.yml` to:

  * Check Python version.
  * Install dependencies from `requirements.txt`.
  * Ensure the environment is reproducible and ready for future tasks.



### **✅ Key Deliverables for Task 1**

* A working GitHub repo with branches and PRs.
* Proper folder structure and essential files.
* Virtual environment ready.
* CI workflow in place.
* Clean, professional commit history demonstrating project hygiene.

