<script setup>
const steps = [
  'Lead',
  'Registration',
  'Appointment',
  'Consultation',
  'Lab',
  'Pharmacy',
  'Billing',
  'Follow-up',
]
</script>

<template>
  <section id="workflow" class="scroll-mt-24 bg-white py-20 lg:py-28">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="mx-auto max-w-3xl text-center">
        <p class="text-sm font-bold uppercase tracking-[0.18em] text-health-purple">
          Connected care journey
        </p>
        <h2 class="mt-3 text-3xl font-extrabold tracking-tight text-health-deep sm:text-4xl">
          Keep each step in view
        </h2>
        <p class="mt-4 text-lg leading-8 text-health-muted">
          Follow the patient journey across teams, clinical services, and
          operational workflows.
        </p>
      </div>

      <ol class="mt-12 grid gap-3 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-8">
        <li v-for="(step, index) in steps" :key="step"
          class="relative flex min-h-32 flex-col items-center justify-center rounded-2xl border border-health-border bg-health-bg px-4 py-5 text-center">
          <span
            class="inline-flex h-9 w-9 items-center justify-center rounded-full bg-health-gradient text-sm font-bold text-white">
            {{ String(index + 1).padStart(2, '0') }}
          </span>
          <span class="mt-3 text-sm font-semibold text-health-deep">{{ step }}</span>
          <svg v-if="index < steps.length - 1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round"
            class="absolute -right-3 top-1/2 z-10 hidden h-6 w-6 -translate-y-1/2 text-health-pink lg:block"
            aria-hidden="true">
            <path d="M5 12h14M13 6l6 6-6 6" />
          </svg>
        </li>
      </ol>
    </div>
  </section>
</template>
