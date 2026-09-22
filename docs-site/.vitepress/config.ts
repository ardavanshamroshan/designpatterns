import { defineConfig } from 'vitepress'

const repo = 'https://github.com/ardavanshamroshan/designpatterns'
const base = '/designpatterns/'

export default defineConfig({
  title: 'Design Patterns',
  description: 'SOLID principles and classic design patterns — interactive Python tutorials.',
  base,
  outDir: '../docs',
  cleanUrls: true,
  lastUpdated: true,
  ignoreDeadLinks: true,

  markdown: {
    theme: {
      light: 'github-dark',
      dark: 'github-dark',
    },
  },

  head: [
    ['link', { rel: 'icon', href: `${base}favicon.svg`, type: 'image/svg+xml' }],
    ['meta', { name: 'theme-color', content: '#f4f6f8' }],
  ],

  themeConfig: {
    logo: '/images/logo-mark.svg',
    siteTitle: 'Design Patterns',
    nav: [
      { text: 'SOLID', link: '/solid/' },
      { text: 'Catalog', link: '/patterns/' },
      { text: 'GitHub', link: repo },
    ],

    sidebar: [
      {
        text: 'Start',
        items: [
          { text: 'Home', link: '/' },
          { text: 'SOLID', link: '/solid/' },
          { text: 'Catalog', link: '/patterns/' },
        ],
      },
      {
        text: 'SOLID',
        items: [
          { text: 'Single Responsibility', link: '/solid/srp' },
          { text: 'Open / Closed', link: '/solid/ocp' },
          { text: 'Liskov Substitution', link: '/solid/lsp' },
          { text: 'Interface Segregation', link: '/solid/#interface-segregation' },
          { text: 'Dependency Inversion', link: '/solid/#dependency-inversion' },
        ],
      },
      {
        text: 'Patterns',
        items: [
          { text: 'Catalog', link: '/patterns/' },
          { text: 'Creational', link: '/patterns/#creational' },
          { text: 'Structural', link: '/patterns/#structural' },
          { text: 'Behavioral', link: '/patterns/#behavioral' },
        ],
      },
    ],

    socialLinks: [{ icon: 'github', link: repo }],

    search: {
      provider: 'local',
      options: { detailedView: true },
    },

    footer: {
      message:
        'Built by <a href="https://ardavanshamroshan.ir" target="_blank" rel="noopener">Ardavan ShamRoshan</a> · <a href="https://github.com/ardavanshamroshan" target="_blank" rel="noopener">GitHub</a>',
      copyright: '© Design Patterns tutorials',
    },

    outline: {
      level: [2, 3],
      label: 'On this page',
    },
  },
})
