<template>
  <section id="home"
    class="relative scroll-mt-24 overflow-hidden bg-health-bg pb-16 pt-28 sm:pb-20 sm:pt-30 lg:pb-16  lg:pt-34">
    <div
      class="pointer-events-none absolute -right-36 -top-32 h-[440px] w-[440px] rounded-full bg-health-gradient-soft blur-3xl"
      aria-hidden="true" />
    <div
      class="pointer-events-none absolute -bottom-28 -left-36 h-[360px] w-[360px] rounded-full bg-fuchsia-100/50 blur-3xl"
      aria-hidden="true" />

    <div
      class="relative mx-auto grid max-w-7xl items-center gap-12 px-4 sm:px-6 lg:grid-cols-[0.9fr_1.1fr] lg:gap-16 lg:px-8">
      <div>
        <p
          class="inline-flex items-center gap-2 rounded-full border border-health-border bg-white px-4 py-1.5 text-sm font-semibold text-health-purple shadow-sm">
          <span class="h-2 w-2 rounded-full bg-health-pink" aria-hidden="true" />
          AI-Powered Healthcare Management System
        </p>

        <h1
          class="mt-6 text-4xl font-extrabold leading-tight tracking-tight text-health-deep sm:text-5xl xl:text-[50px]">
          AI-powered healthcare for
          <span class="bg-health-gradient bg-clip-text text-transparent">better care</span>
        </h1>

        <p class="mt-6 max-w-2xl text-lg leading-8 text-health-muted">
          Bring patient records, appointments, clinical workflows, billing,
          pharmacy, and hospital operations together in one AI-powered healthcare workspace.
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
        <div class="rounded-[25px] bg-health-gradient p-1.5 shadow-health-panel">
          <div class="overflow-hidden rounded-[22px]  bg-white p-2 sm:p-2">
            <img class="block h-auto w-full rounded-xl" :src="'/files/Healthcare-Operations-Dashboard.png'"
              alt="Healthcare Operations Dashboard" />
          </div>
        </div>
      </div>

    </div>
  </section>
</template>


<script setup>
import { useLoginUrl } from '@/composables/useLoginUrl'

const { loginUrl } = useLoginUrl()
const highlights = ['AI-powered insights', 'Patient-first workflows', 'Connected hospital operations']
</script>