<script setup lang="ts">
import { ref } from 'vue'

defineProps<{
  badTitle?: string
  goodTitle?: string
}>()

const tab = ref<'bad' | 'good'>('bad')
</script>

<template>
  <div class="ix-compare">
    <div class="ix-compare__tabs" role="tablist">
      <button
        type="button"
        role="tab"
        :aria-selected="tab === 'bad'"
        @click="tab = 'bad'"
      >
        {{ badTitle || 'Violation' }}
      </button>
      <button
        type="button"
        role="tab"
        :aria-selected="tab === 'good'"
        @click="tab = 'good'"
      >
        {{ goodTitle || 'Compliant' }}
      </button>
    </div>
    <div v-show="tab === 'bad'" class="ix-compare__panel" role="tabpanel">
      <slot name="bad" />
    </div>
    <div v-show="tab === 'good'" class="ix-compare__panel" role="tabpanel">
      <slot name="good" />
    </div>
  </div>
</template>
