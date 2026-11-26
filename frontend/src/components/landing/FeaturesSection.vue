<template>
  <section class="scroll-mt-24 bg-white py-16 lg:py-12">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div id="features" class="mx-auto max-w-3xl text-center">
        <p class="text-sm font-bold uppercase tracking-[0.18em] text-health-purple">
          AI-Powered Healthcare Management System Features
        </p>
        <h2 class="mt-3 text-3xl font-extrabold tracking-tight text-health-deep sm:text-7xl">
          The tools to coordinate
          <span class="bg-health-gradient bg-clip-text text-transparent">care and operations</span>
        </h2>
        <p class="mt-4 text-lg leading-8 text-health-muted">
          Explore capabilities across patient care, hospital administration,
          finance, pharmacy, reporting, and security in one AI-powered workspace.
        </p>
      </div>

      <div class="mt-10 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        <article v-for="(feature, index) in features" :key="feature.title"
          class="group rounded-2xl border border-health-border bg-white p-6 shadow-health-card transition-all duration-300 hover:-translate-y-1 hover:border-health-pink/50 hover:shadow-health-panel">
          <div class="flex items-start justify-between gap-4">
            <span
              class="inline-flex h-12 w-12 shrink-0 items-center justify-center rounded-xl transition-transform duration-300 group-hover:scale-105"
              :class="feature.accent" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"
                stroke-linejoin="round" class="h-6 w-6">
                <template v-if="feature.icon === 'patient'">
                  <circle cx="12" cy="7" r="4" />
                  <path d="M5 21v-2a7 7 0 0 1 14 0v2M12 14v4M10 16h4" />
                </template>
                <template v-else-if="feature.icon === 'billing'">
                  <rect x="3" y="4" width="18" height="16" rx="2" />
                  <path d="M7 9h10M7 13h4M7 16h2M15 13v4M13 15h4" />
                </template>
                <template v-else-if="feature.icon === 'pharmacy'">
                  <path d="m10 3 11 11-7 7L3 10V3h7Z" />
                  <circle cx="7" cy="7" r="1" />
                  <path d="m10 10 5 5M13 7l4 4" />
                </template>
                <template v-else-if="feature.icon === 'analytics'">
                  <path d="M3 3v18h18M8 15l4-4 3 3 6-7" />
                  <path d="M17 7h4v4" />
                </template>
                <template v-else-if="feature.icon === 'finance'">
                  <rect x="3" y="5" width="18" height="14" rx="2" />
                  <path d="M3 10h18M7 15h4M16 14v3M14.5 15.5h3" />
                </template>
                <template v-else-if="feature.icon === 'inpatient'">
                  <path d="M3 20V5M3 17h18v3M5 12h14a2 2 0 0 1 2 2v3M5 17v-5a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v5M7 7h3" />
                  <path d="M7 5v4" />
                </template>
                <template v-else-if="feature.icon === 'emergency'">
                  <path d="M12 22s8-4 8-11V5l-8-3-8 3v6c0 7 8 11 8 11Z" />
                  <path d="M12 7v8M8 11h8" />
                </template>
                <template v-else-if="feature.icon === 'staff'">
                  <circle cx="9" cy="8" r="3" />
                  <path d="M3 20v-1a6 6 0 0 1 12 0v1M16 5.5a3 3 0 0 1 0 5.8M18 14a5 5 0 0 1 3 4.6v1" />
                </template>
                <template v-else>
                  <rect x="4" y="10" width="16" height="11" rx="2" />
                  <path d="M8 10V7a4 4 0 0 1 8 0v3M12 14v3" />
                </template>
              </svg>
            </span>
            <span class="mt-1 text-xs font-bold tabular-nums tracking-wide text-health-muted/70">
              {{ String(index + 1).padStart(2, '0') }}
            </span>
          </div>

          <h3 class="mt-5 text-lg font-bold text-health-deep">{{ feature.title }}</h3>
          <ul class="mt-4 grid gap-2.5 sm:grid-cols-2">
            <li v-for="item in feature.items" :key="item"
              class="flex items-start gap-2 text-sm leading-5 text-health-muted">
              <svg viewBox="0 0 20 20" fill="none" class="mt-0.5 h-4 w-4 shrink-0 text-health-purple"
                aria-hidden="true">
                <path d="m16.5 5.5-8 9-4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                  stroke-linejoin="round" />
              </svg>
              {{ item }}
            </li>
          </ul>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
const features = [
  {
    title: 'Patient Management',
    icon: 'patient',
    accent: 'bg-violet-50 text-violet-700',
    items: [
      'Patient Registration',
      'Appointment Scheduling',
      'Electronic Medical Records',
      'Treatment History',
      'Admission & Discharge',
      'Patient Tracking',
    ],
  },
  {
    title: 'Billing & Revenue',
    icon: 'billing',
    accent: 'bg-fuchsia-50 text-fuchsia-700',
    items: [
      'Invoice Generation',
      'Insurance Claims',
      'Payment Tracking',
      'Revenue Reports',
      'Tax Compliance',
      'Outstanding Monitoring',
    ],
  },
  {
    title: 'Pharmacy Management',
    icon: 'pharmacy',
    accent: 'bg-purple-50 text-purple-700',
    items: [
      'Medicine Stock',
      'Batch Tracking',
      'Expiry Alerts',
      'Barcode Support',
      'Supplier Tracking',
      'Inventory Reports',
    ],
  },
  {
    title: 'Analytics & Reports',
    icon: 'analytics',
    accent: 'bg-pink-50 text-pink-700',
    items: [
      'Dashboard Insights',
      'Department Reports',
      'Revenue Analytics',
      'Performance Metrics',
      'Patient Statistics',
      'Real-time Monitoring',
    ],
  },
  {
    title: 'Finance & Accounting',
    icon: 'finance',
    accent: 'bg-violet-100 text-violet-800',
    items: [
      'Ledger Management',
      'Expense Tracking',
      'Cash Flow Monitoring',
      'GST Reports',
      'Budget Planning',
      'Automated Accounting',
    ],
  },
  {
    title: 'Inpatient Management',
    icon: 'inpatient',
    accent: 'bg-fuchsia-100 text-fuchsia-800',
    items: [
      'Bed Allocation',
      'Ward Management',
      'Nursing Records',
      'Treatment Monitoring',
      'Discharge Summary',
      'IP Billing',
    ],
  },
  {
    title: 'Emergency Services',
    icon: 'emergency',
    accent: 'bg-rose-50 text-rose-700',
    items: [
      'Emergency Registration',
      'Ambulance Tracking',
      'Critical Care Monitoring',
      'Quick Billing',
      'Emergency Reports',
      'Patient Alerts',
    ],
  },
  {
    title: 'Doctor & Staff Management',
    icon: 'staff',
    accent: 'bg-purple-100 text-purple-800',
    items: [
      'Staff Scheduling',
      'Payroll Integration',
      'Department Allocation',
      'Performance Tracking',
      'Attendance Monitoring',
      'Role Permissions',
    ],
  },
  {
    title: 'Compliance & Security',
    icon: 'security',
    accent: 'bg-pink-100 text-pink-800',
    items: [
      'Data Protection',
      'Audit Trails',
      'Regulatory Compliance',
      'Access Control',
      'Backup & Recovery',
      'Quality Monitoring',
    ],
  },
]
</script>