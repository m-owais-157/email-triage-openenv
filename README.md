---
title: Email Triage OpenEnv
emoji: 📧
colorFrom: blue
colorTo: green
sdk: docker
app_file: main.py
---

# 📧 Smart Email Triage Environment

## 🚀 Overview
This project simulates an intelligent email classification environment where an agent learns to categorize emails into:
- Spam
- Important
- Normal

## 🎯 Objective
Train an agent to maximize reward by correctly classifying emails based on real-world patterns.

## ⚙️ Environment Design
- `/reset`: Initializes environment with unseen emails
- `/step`: Takes action and returns reward
- `/state`: Tracks progress

## 🧠 Reward System
- Correct classification → +2
- Misclassifying spam → -3 (high risk)
- Other mistakes → -1

## 🔥 Key Features
- Realistic email dataset (OTP, scams, promotions)
- Noisy and tricky inputs
- Risk-aware reward design

## 🤖 Agent
A rule-based agent is implemented in `inference.py` to interact with the environment.

## 🏁 Goal
Maximize total reward across all steps.
