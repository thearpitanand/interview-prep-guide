# AI/ML Interview Prep

Two paths to the same destination. Pick the one that fits your timeline.

---

## Choose Your Path

| Path | Time | Best For | Start Here |
|------|------|----------|------------|
| **[Crash Course](./crash-course/01-the-complete-guide.md)** | 5 hours | Visual learners, time-constrained, SWEs new to ML | [Start Crash Course ->](./crash-course/00-README.md) |
| **[Deep Dive](./deep-dive/00-README.md)** | 6+ hours | Comprehensive coverage, reference material, detailed theory | [Start Deep Dive ->](./deep-dive/00-README.md) |

---

## Crash Course (Recommended for Interview Prep)

One consolidated guide. Visual-first with mermaid diagrams, ASCII art, SWE analogies, and worked examples. Everything interconnects.

| Hour | Topic | Key Concepts |
|------|-------|-------------|
| 1 | Foundations | ML types, pipeline, metrics, bias-variance |
| 2 | Classical Algorithms | 9 algorithms with visuals, selection flowchart |
| 3 | Modern AI | CNNs, Transformers, BERT, GPT, RAG, RLHF |
| 4 | ML in Production | System design framework, MLOps, gotchas |
| 5 | Interview Mastery | Top 25 questions, answer framework, cheat sheet |
| + | [Implementation Stories](./crash-course/02-implementation-stories.md) | 2 showcase projects: Churn Predictor & RAG Q&A System |

**[Open the Complete Guide ->](./crash-course/01-the-complete-guide.md)**

---

## Deep Dive (Comprehensive Reference)

Nine detailed topic files covering every area in depth. Use as reference material or for thorough study.

| # | Topic | Time | Priority |
|---|-------|------|----------|
| -- | [Beginner Start Here](./deep-dive/BEGINNER-START-HERE.md) | 30 min | START |
| 01 | [ML Fundamentals](./deep-dive/01-ml-fundamentals.md) | 45 min | HIGH |
| 02 | [Classical ML Algorithms](./deep-dive/02-classical-algorithms.md) | 50 min | HIGH |
| 03 | [Deep Learning](./deep-dive/03-deep-learning.md) | 60 min | HIGH |
| 04 | [NLP & LLMs](./deep-dive/04-nlp-and-llms.md) | 40 min | HIGH |
| 05 | [Computer Vision](./deep-dive/05-computer-vision.md) | 30 min | MEDIUM |
| 06 | [ML System Design & MLOps](./deep-dive/06-ml-system-design.md) | 45 min | HIGH |
| 07 | [Math & Statistics](./deep-dive/07-math-and-statistics.md) | 30 min | MEDIUM |
| 08 | [Practical Coding](./deep-dive/08-practical-coding.md) | 40 min | HIGH |
| 09 | [Behavioral & Scenarios](./deep-dive/09-behavioral-scenarios.md) | 20 min | MEDIUM |

**[Open Deep Dive Guide ->](./deep-dive/00-README.md)**

---

## Quick Reference

### The Big 5 Concepts

1. **Bias-Variance Tradeoff** -- High bias = underfitting, High variance = overfitting
2. **Transformer Architecture** -- Self-attention: softmax(QK^T/sqrt(d_k))V
3. **Evaluation Metrics** -- Precision (FP costly) vs Recall (FN costly)
4. **Gradient Descent & Backprop** -- Forward pass -> loss -> backward pass -> update
5. **ML System Design** -- Requirements -> Data -> Features -> Model -> Eval -> Deploy -> Monitor

### Key Formulas

| Formula | Expression |
|---------|-----------|
| Precision | TP / (TP + FP) |
| Recall | TP / (TP + FN) |
| F1 Score | 2 * (P * R) / (P + R) |
| Attention | softmax(QK^T / sqrt(d_k)) * V |
| Gradient Update | theta = theta - alpha * grad(L) |
