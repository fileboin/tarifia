# @tarifia-sh/ui

This is the UI library for the Tarifia project.

> [!NOTE]
> This is a private library for the Tarifia project. You probably shouldn't use it directly in your own projects.

## Structure

We use `shadcn/ui` components as a base for our UI. Those raw components are generated in `src/components/ui`.

Our own custom components are located in `src/components/atoms` and `src/components/molecules`.

## How to add/update a shadcn component?

```bash
cd clients/packages/ui
```

```bash
pnpm dlx shadcn@latest add accordion
```
