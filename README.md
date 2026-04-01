# 📊 ANOVA-Based Analysis of Student Performance

## 📌 Project Overview
This project is a **Mathematics Mini-Project** focused on applying **Analysis of Variance (ANOVA)** to a real-world dataset of student performance.

The objective is to analyze how different factors such as **Motivation Level, Sleep, Study Time, and Attendance** influence students' exam scores using statistical methods.

Unlike basic implementations, this project emphasizes:
- Manual ANOVA calculations (SSB, SSW, MSB, MSW)
- Visual interpretation using normal distribution plots
- Real-world analytical conclusions

---

## 🎯 Objectives
- To understand and apply **One-Way ANOVA**
- To compare multiple groups using statistical methods
- To visualize:
  - Within-group variation (SSW)
  - Between-group variation (SSB)
- To interpret **F-statistic and p-value**
- To derive meaningful real-world insights from data

---

## 📂 Project Structure
📁 project-folder
│── 📓 anova_analysis.ipynb
│── 📊 student_performance_data_cat.csv
│── 📄 README.md

---

## 📊 Dataset Description
The dataset contains student-related features such as:
- Motivation Level  
- Study Hours  
- Sleep Hours  
- Attendance  
- Exam Score  

These features are preprocessed into categorical groups (e.g., Low, Medium, High) for ANOVA testing.

---

## 🧠 Methodology

### 1. Data Preparation
- Cleaned and categorized continuous variables into groups
- Selected:
  - Independent variable (factor)
  - Dependent variable (Exam Score)

---

### 2. Hypothesis Testing

For each factor:

- **Null Hypothesis (H₀):**  
  All group means are equal  

- **Alternative Hypothesis (H₁):**  
  At least one group mean is different  

---

### 3. ANOVA Calculations

The following metrics are computed manually:

- SSB (Sum of Squares Between Groups)
- SSW (Sum of Squares Within Groups)
- MSB (Mean Square Between)
- MSW (Mean Square Within)

Then:

- F-statistic = MSB / MSW
- p-value is computed to test significance

---

### 4. Visualization

The project includes:

- 📈 Normal Distribution Curves  
  - One curve per group  
  - Shows spread and mean  

- 📊 Overlapping Distribution Graph  
  - Highlights:
    - Group means  
    - Overall mean  
    - Variance differences  

---

## 📌 Key Results

| Factor        | Result                          |
|--------------|---------------------------------|
| Motivation   | Statistically significant (weak effect) |
| Sleep        | Not significant                 |
| Study Level  | Strongly significant            |
| Attendance   | Extremely significant           |

---

## 🧠 Key Insight

> Statistical significance does not always imply strong practical impact.  
Some factors (like motivation) show significance mathematically but have overlapping distributions, indicating a weaker real-world effect.

---

## ⚙️ How to Run the Project

### 🔹 Step 1: Clone the Repository
git clone <your-repo-link>
cd <repo-folder>

---

### 🔹 Step 2: Install Required Libraries
pip install numpy pandas matplotlib seaborn scipy

---

### 🔹 Step 3: Run the Notebook

#### Option 1: Using Jupyter Notebook
Open:
anova_analysis.ipynb

#### Option 2: Using VS Code
- Open folder in VS Code  
- Open `.ipynb` file  
- Click **Run All**

---

## 📊 Technologies Used
- Python  
- NumPy  
- Pandas  
- Matplotlib  
- Seaborn  
- SciPy  

---

## 🚀 Future Improvements
- Using a bigger dataset like IPL
- Find out the probability of winning team
- What is impact of each player
- How ground conditions effect the match

---

## 📚 Conclusion
This project demonstrates how statistical techniques like ANOVA can be applied to real-world datasets to uncover meaningful patterns and insights. It highlights the importance of combining mathematical rigor with visual interpretation for better decision-making.

---

## 🙌 Acknowledgement
This project was created as part of a **Mathematics Mini Project** to explore practical applications of statistical analysis.

---

## Authors
- Sameer Jagtap
- Chirag Poojary
- Siddharth Shinde
- Shayaan Chitre
- Ashwin Ambastha
- Darshan Palkar