# Action Playground

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