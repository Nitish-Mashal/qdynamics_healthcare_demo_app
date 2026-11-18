<script setup>
import { useLoginUrl } from '@/composables/useLoginUrl'

const { loginUrl } = useLoginUrl()

const highlights = ['Patient-first workflows', 'Connected hospital operations', 'Role-based access']
const overview = [
  { label: 'Appointments', detail: 'OPD schedule', value: 'Today' },
  { label: 'Patient records', detail: 'Registration & history', value: 'Connected' },
  { label: 'Care teams', detail: 'Doctors & staff', value: 'Coordinated' },
]
</script>

<template>
  <section id="home"
    class="relative scroll-mt-24 overflow-hidden bg-health-bg pb-16 pt-28 sm:pb-20 sm:pt-32 lg:pb-24 lg:pt-40">
    <div
      class="pointer-events-none absolute -right-36 -top-32 h-[440px] w-[440px] rounded-full bg-health-gradient-soft blur-3xl"
      aria-hidden="true" />
    <div
      class="pointer-events-none absolute -bottom-28 -left-36 h-[360px] w-[360px] rounded-full bg-fuchsia-100/50 blur-3xl"
      aria-hidden="true" />

    <div
      class="relative mx-auto grid max-w-7xl items-center gap-12 px-4 sm:px-6 lg:grid-cols-[1.05fr_0.95fr] lg:gap-16 lg:px-8">
      <div>
        <p
          class="inline-flex items-center gap-2 rounded-full border border-health-border bg-white px-4 py-1.5 text-sm font-semibold text-health-purple shadow-sm">
          <span class="h-2 w-2 rounded-full bg-health-pink" aria-hidden="true" />
          Healthcare Management System
        </p>

        <h1 class="mt-6 text-4xl font-extrabold leading-tight tracking-tight text-health-deep sm:text-5xl xl:text-6xl">
          Connected systems for
          <span class="bg-health-gradient bg-clip-text text-transparent">better care</span>
        </h1>

        <p class="mt-6 max-w-2xl text-lg leading-8 text-health-muted">
          Bring patient records, appointments, clinical workflows, billing,
          pharmacy, and hospital operations together in one healthcare workspace.
        </p>

        <div class="mt-8 flex flex-col gap-3 sm:flex-row sm:items-center">
          <a :href="loginUrl"
            class="inline-flex items-center justify-center gap-2 rounded-xl bg-health-gradient px-6 py-2.5 text-base font-semibold text-white shadow-health-panel transition-transform duration-200 hover:-translate-y-0.5 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-health-purple focus-visible:ring-offset-2">
            Open Demo App
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
              stroke-linejoin="round" class="h-4 w-4" aria-hidden="true">
              <path d="M5 12h14M13 6l6 6-6 6" />
            </svg>
          </a>
          <a href="https://www.quantumberg.com/Contact"
            class="inline-flex items-center justify-center rounded-xl border-2 border-health-border bg-white px-6 py-2.5 text-base font-semibold text-health-ink transition-colors hover:border-health-purple hover:text-health-purple focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-health-purple focus-visible:ring-offset-2">
            Request a Demo
          </a>
        </div>

        <ul class="mt-8 flex flex-wrap items-center gap-x-5 gap-y-2">
          <li v-for="highlight in highlights" :key="highlight"
            class="inline-flex items-center gap-1.5 text-sm font-medium text-health-muted">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"
              stroke-linejoin="round" class="h-3.5 w-3.5 text-health-purple" aria-hidden="true">
              <path d="m20 6-11 11-5-5" />
            </svg>
            {{ highlight }}
          </li>
        </ul>
      </div>

      <div class="relative">
        <div class="rounded-[28px] bg-health-gradient p-1.5 shadow-health-panel">
          <div class="overflow-hidden rounded-[22px] border border-white/60 bg-white p-5 sm:p-7" role="img"
            aria-label="Illustrative healthcare dashboard preview with connected patient, appointment, care team, and operations views">
            <div class="flex items-start justify-between gap-3">
              <div>
                <p class="text-xs font-bold uppercase tracking-[0.16em] text-health-purple">
                  Healthcare workspace
                </p>
                <h2 class="mt-2 text-xl font-extrabold text-health-deep sm:text-2xl">
                  Care, connected
                </h2>
              </div>
              <span
                class="inline-flex items-center gap-2 rounded-full bg-health-gradient-soft px-3 py-1.5 text-xs font-semibold text-health-purple">
                <span class="h-2 w-2 rounded-full bg-health-pink" aria-hidden="true" />
                Sample view
              </span>
            </div>

            <div class="mt-6 grid grid-cols-3 gap-3">
              <div v-for="(item, index) in overview" :key="item.label"
                class="rounded-2xl border border-health-border bg-health-bg p-3 sm:p-4">
                <span class="inline-flex h-9 w-9 items-center justify-center rounded-xl"
                  :class="index === 0 ? 'bg-violet-100 text-violet-700' : index === 1 ? 'bg-fuchsia-100 text-fuchsia-700' : 'bg-purple-100 text-purple-700'"
                  aria-hidden="true">
                  <svg v-if="index === 0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                    stroke-linecap="round" stroke-linejoin="round" class="h-5 w-5">
                    <rect x="3" y="5" width="18" height="16" rx="2" />
                    <path d="M16 3v4M8 3v4M3 11h18" />
                  </svg>
                  <svg v-else-if="index === 1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                    stroke-linecap="round" stroke-linejoin="round" class="h-5 w-5">
                    <path d="M12 21s-8-4.5-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 6.5-8 11-8 11Z" />
                  </svg>
                  <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"
                    stroke-linecap="round" stroke-linejoin="round" class="h-5 w-5">
                    <circle cx="9" cy="8" r="3" />
                    <path d="M3 20v-1a6 6 0 0 1 12 0v1M16 5.5a3 3 0 0 1 0 5.8M18 14a5 5 0 0 1 3 4.6v1" />
                  </svg>
                </span>
                <p class="mt-4 text-sm font-bold text-health-deep">{{ item.label }}</p>
                <p class="mt-1 text-xs leading-5 text-health-muted">{{ item.detail }}</p>
                <p class="mt-3 text-xs font-semibold text-health-purple">{{ item.value }}</p>
              </div>
            </div>

            <div class="mt-5 rounded-2xl border border-health-border p-4">
              <div class="flex items-center justify-between gap-4">
                <div>
                  <p class="text-sm font-bold text-health-deep">One connected care journey</p>
                  <p class="mt-1 text-xs text-health-muted">From first appointment to follow-up</p>
                </div>
                <span
                  class="inline-flex h-10 w-10 items-center justify-center rounded-full bg-health-gradient-soft text-health-purple"
                  aria-hidden="true">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"
                    stroke-linejoin="round" class="h-5 w-5">
                    <path d="M4 12h16M14 6l6 6-6 6" />
                  </svg>
                </span>
              </div>
              <div class="mt-4 h-2 overflow-hidden rounded-full bg-health-bg">
                <div class="h-full w-4/5 rounded-full bg-health-gradient" />
              </div>
              <div class="mt-2 flex justify-between text-[10px] font-medium text-health-muted">
                <span>Registration</span>
                <span>Consultation</span>
                <span>Follow-up</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
