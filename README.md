# Action Playground
[![Tests on all OS](https://github.com/Alex-AMC/action_playground/actions/workflows/Alex_Dev_Matrix_test.yml/badge.svg?branch=Alex_Dev)](https://github.com/Alex-AMC/action_playground/actions/workflows/Alex_Dev_Matrix_test.yml)
[![Tests with Conda](https://github.com/Alex-AMC/action_playground/actions/workflows/Alex_dev_tests.yml/badge.svg?branch=Alex_Dev)](https://github.com/Alex-AMC/action_playground/actions/workflows/Alex_dev_tests.yml)

Objectives: (Stolen from Ben)
- Run tests on MR to develop
- Build container and test container output
- Upload image to container registry (develop)
- Merge develop to release branch
- Run tests on MR to release branch
- Build release container
- Upload image to container registry (release)
- Build docs
- Upload docs to wiki or pages or wherever
- Merge release to main
- Set manual gate
- On manual accept -> Run tests on MR to main
- 1. Build release container
- Upload image to container registry (stable)
- Build docs
- Upload docs to wiki or pages or wherever (As `stable` or similar)