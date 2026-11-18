<script setup>
const roles = [
  {
    title: 'Admin',
    description: 'Operational oversight across teams and departments.',
    actions: ['Manage hospital operations', 'Generate reports', 'Control user permissions', 'Monitor analytics'],
    icon: 'admin',
  },
  {
    title: 'Labratory',
    description: 'Tools for managing lab requests, samples, and results.',
    actions: ['Manage lab requests', 'Process samples', 'Record test results', 'Publish lab reports'],
    icon: 'laboratory',
  },
  {
    title: 'Frontdesk',
    description: 'Tools to welcome patients and coordinate their visits.',
    actions: ['Register patients', 'Schedule appointments', 'Check in visitors', 'Coordinate patient flow'],
    icon: 'frontdesk',
  },
]
</script>

<template>
  <section id="roles" class="scroll-mt-24 bg-health-bg py-20 lg:py-28">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="mx-auto max-w-3xl text-center">
        <p class="text-sm font-bold uppercase tracking-[0.18em] text-health-purple">
          Role-based access
        </p>
        <h2 class="mt-3 text-3xl font-extrabold tracking-tight text-health-deep sm:text-4xl">
          A workspace for every part of care
        </h2>
        <p class="mt-4 text-lg leading-8 text-health-muted">
          Admin, laboratory, and frontdesk teams can focus on the tasks and
          information relevant to their role.
        </p>
      </div>

      <div class="mt-12 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        <article v-for="role in roles" :key="role.title"
          class="rounded-2xl border border-health-border bg-white p-6 shadow-health-card">
          <span
            class="inline-flex h-11 w-11 items-center justify-center rounded-xl bg-health-gradient-soft text-health-purple"
            aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"
              stroke-linejoin="round" class="h-5 w-5">
              <template v-if="role.icon === 'laboratory'">
                <path d="M9 3h6M10 3v7.5l-4.5 7A2.3 2.3 0 0 0 7.4 21h9.2a2.3 2.3 0 0 0 1.9-3.5l-4.5-7V3" />
                <path d="M8 15h8M10 11h4" />
              </template>
              <template v-else-if="role.icon === 'frontdesk'">
                <circle cx="12" cy="8" r="3.5" />
                <path d="M4 21v-1a8 8 0 0 1 16 0v1M18 5h3M19.5 3.5v3" />
              </template>
              <template v-else>
                <rect x="3" y="3" width="8" height="8" rx="1.5" />
                <rect x="13" y="3" width="8" height="5" rx="1.5" />
                <rect x="13" y="10" width="8" height="11" rx="1.5" />
                <rect x="3" y="13" width="8" height="8" rx="1.5" />
              </template>
            </svg>
          </span>
          <h3 class="mt-5 text-lg font-bold text-health-deep">{{ role.title }}</h3>
          <p class="mt-2 text-sm leading-6 text-health-muted">{{ role.description }}</p>
          <ul class="mt-5 space-y-2.5">
            <li v-for="action in role.actions" :key="action" class="flex gap-2 text-sm leading-5 text-health-ink">
              <span class="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-health-pink" aria-hidden="true" />
              {{ action }}
            </li>
          </ul>
        </article>
      </div>
    </div>
  </section>
</template>
