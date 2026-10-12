# Profile Definition

## Overview

ResumeLens defines four professional profiles for candidate classification. Each profile is configured in `config/profiles.json` and contains three attributes:

- **Domain:** The professional area associated with the profile.
- **Required qualifications:** The canonical qualifications that must be present for the profile to be recognized.
- **Qualification order:** The sequence in which qualifications are expected during profile classification.

The profile definitions used by the current implementation are described below.

## 1. Full Stack Developer

**Domain:** Software Engineering

**Required qualifications:**
- `JAVASCRIPT`
- `REACT`
- `NODE_JS`
- `POSTGRESQL`
- `GIT`

**Qualification order:**

`JAVASCRIPT → REACT → NODE_JS → POSTGRESQL → GIT`

A candidate matches this profile when the implementation recognizes the required qualifications in the configured order.

## 2. Machine Learning Engineer

**Domain:** AI/Data

**Required qualifications:**
- `PYTHON`
- `PANDAS`
- `SCIKIT_LEARN`
- `TENSORFLOW`
- `POSTGRESQL`
- `GIT`

**Qualification order:**

`PYTHON → PANDAS → SCIKIT_LEARN → TENSORFLOW → POSTGRESQL → GIT`

A candidate matches this profile when the implementation recognizes the required qualifications in the configured order.

## 3. Backend Developer

**Domain:** Software Engineering

**Required qualifications:**
- `PYTHON`
- `FASTAPI`
- `POSTGRESQL`
- `REST_API`
- `DOCKER`
- `GIT`

**Qualification order:**

`PYTHON → FASTAPI → POSTGRESQL → REST_API → DOCKER → GIT`

A candidate matches this profile when the implementation recognizes the required qualifications in the configured order.

## 4. Data Scientist

**Domain:** AI/Data

**Required qualifications:**
- `PYTHON`
- `PANDAS`
- `NUMPY`
- `SCIKIT_LEARN`
- `SQL`
- `GIT`

**Qualification order:**

`PYTHON → PANDAS → NUMPY → SCIKIT_LEARN → SQL → GIT`

A candidate matches this profile when the implementation recognizes the required qualifications in the configured order.

## Shared Classification Rules

Some qualifications, such as `PYTHON`, `PANDAS`, `POSTGRESQL`, and `GIT`, can appear in more than one profile.

Therefore, qualifications are not necessarily exclusive to a single professional profile. Classification depends on the required qualifications and their configured order for each profile.

ResumeLens identifies matching qualification patterns. It does not rank candidates or make hiring decisions.
