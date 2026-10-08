# Git Flow + CI/CD example

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


- `ci-feature.yml` — runs on `feature/**` branches and pull requests
- `ci-develop.yml` — runs on pushes to `develop`
- `cd-staging.yml` — runs on `release/**` branches
- `cd-production.yml` — runs on `main` and `hotfix/**`

