# Git Flow + CI/CD example

This repository demonstrates a simple multi-branch CI/CD setup using a Git Flow model:

- `feature/*` — new features and bug fixes are developed here
- `develop` — integration branch for tested code
- `release/*` — release preparation and staging validation
- `main` — production-ready code
- `hotfix/*` — emergency fixes for production

## Project structure

- `app/` — sample Python application
- `tests/` — automated checks
- `.github/workflows/` — GitHub Actions pipelines for CI and CD

## CI/CD flow

1. A developer creates a feature branch such as `feature/login-form`.
2. Pushes code to GitHub.
3. CI runs automatically on the feature branch.
4. When ready, the feature is merged into `develop`.
5. CI on `develop` validates the branch.
6. A `release/*` branch triggers staging deployment.
7. After release approval, the code is merged into `main` and deployed to production.
8. `hotfix/*` handles critical production fixes.

## Local validation

Run:

```bash
python -m unittest discover -s tests -v
```

## GitHub workflows

The workflows are configured to simulate the following:

- `ci-feature.yml` — runs on `feature/**` branches and pull requests
- `ci-develop.yml` — runs on pushes to `develop`
- `cd-staging.yml` — runs on `release/**` branches
- `cd-production.yml` — runs on `main` and `hotfix/**`

## Example branch sequence

```bash
git checkout develop
git checkout -b feature/login-form
git push -u origin feature/login-form
git checkout develop
git merge --no-ff feature/login-form
git checkout -b release/1.0.0
git push -u origin release/1.0.0
git checkout main
git merge --no-ff release/1.0.0
git checkout -b hotfix/1.0.1
git push -u origin hotfix/1.0.1
```

## Notes

This is a minimal example intended to show the structure and automation logic rather than a production-grade deployment system.
