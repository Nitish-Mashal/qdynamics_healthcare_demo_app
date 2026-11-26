

<template>
  <section class="scroll-mt-24 bg-health-bg py-16 lg:py-12">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div id="benefits" class="mx-auto max-w-3xl text-center">
        <p class="text-sm font-bold uppercase tracking-[0.18em] text-health-purple">
          Benefits
        </p>
        <h2 class="mt-3 text-3xl font-extrabold tracking-tight text-health-deep sm:text-7xl">
          Connected care, enhanced by AI
        </h2>
        <p class="mt-4 text-lg leading-8 text-health-muted">
          Pair connected healthcare workflows with AI-powered capabilities that support everyday operations.
        </p>
      </div>

      <div class="mt-10 grid gap-5 md:grid-cols-3">
        <article v-for="benefit in benefits" :key="benefit.title"
          class="rounded-2xl border border-health-border bg-white p-6 shadow-health-card">
          <span
            class="inline-flex h-12 w-12 items-center justify-center rounded-xl bg-health-gradient-soft text-health-purple"
            aria-hidden="true">
            <svg v-if="benefit.icon === 'connected'" viewBox="0 0 24 24" fill="none" stroke="currentColor"
              stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="h-6 w-6">
              <circle cx="6" cy="12" r="3" />
              <circle cx="18" cy="6" r="3" />
              <circle cx="18" cy="18" r="3" />
              <path d="m8.7 10.7 6.6-3.4M8.7 13.3l6.6 3.4" />
            </svg>
            <svg v-else-if="benefit.icon === 'operations'" viewBox="0 0 24 24" fill="none" stroke="currentColor"
              stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" class="h-6 w-6">
              <rect x="3" y="4" width="18" height="16" rx="2" />
              <path d="M7 8h10M7 12h4M7 16h2M16 12v4M14.5 14h3" />
            </svg>
            <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"
              stroke-linejoin="round" class="h-6 w-6">
              <path d="M3 3v18h18M8 15l4-4 3 3 6-7" />
              <path d="M17 7h4v4" />
            </svg>
          </span>
          <h3 class="mt-5 text-lg font-bold text-health-deep">{{ benefit.title }}</h3>
          <p class="mt-2 text-sm leading-6 text-health-muted">{{ benefit.description }}</p>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
const benefits = [
  {
    title: 'A more connected experience',
    description: 'Bring patient information and care activities together in one healthcare workspace.',
    icon: 'connected',
  },
  {
    title: 'Simpler daily operations',
    description: 'Coordinate appointments, billing, pharmacy, and hospital workflows in one place.',
    icon: 'operations',
  },
  {
    title: 'AI-powered insights',
    description: 'Pair AI-powered capabilities with reports and dashboards to understand activity across your healthcare organization.',
    icon: 'insight',
  },
]
</script>