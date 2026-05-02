/**
 * main.js — Vanilla JS for Shikhar Kanaujia Portfolio
 * - Nav hide/show on scroll
 * - Active section highlighting
 * - Scroll reveal animations
 * - Mobile nav toggle
 */

(function () {
  'use strict';

  /* ---- NAV HIDE/SHOW ON SCROLL ---- */
  const nav = document.getElementById('main-nav');
  let lastScrollY = 0;
  let ticking = false;

  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const currentY = window.scrollY;
        if (currentY > lastScrollY && currentY > 80) {
          nav.classList.add('hidden');
        } else {
          nav.classList.remove('hidden');
        }
        lastScrollY = currentY;
        ticking = false;
      });
      ticking = true;
    }
  });

  /* ---- ACTIVE SECTION HIGHLIGHTING ---- */
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-links a[href^="#"]');

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          navLinks.forEach((link) => {
            link.classList.toggle(
              'active',
              link.getAttribute('href') === `#${id}`
            );
          });
        }
      });
    },
    { rootMargin: '-40% 0px -55% 0px' }
  );

  sections.forEach((section) => observer.observe(section));

  /* ---- SCROLL REVEAL ---- */
  const revealEls = document.querySelectorAll('.reveal');
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { rootMargin: '0px 0px -80px 0px' }
  );

  revealEls.forEach((el) => revealObserver.observe(el));

  /* ---- MOBILE NAV TOGGLE ---- */
  const toggle = document.getElementById('nav-toggle');
  const linksList = document.querySelector('.nav-links');

  if (toggle && linksList) {
    toggle.addEventListener('click', () => {
      linksList.classList.toggle('open');
    });
    // Close on link click
    linksList.querySelectorAll('a').forEach((a) => {
      a.addEventListener('click', () => linksList.classList.remove('open'));
    });
  }

  /* ---- CONTACT FORM SUCCESS AUTO-DISMISS ---- */
  const successMsg = document.querySelector('.success-msg');
  if (successMsg) {
    setTimeout(() => {
      successMsg.style.transition = 'opacity 0.5s';
      successMsg.style.opacity = '0';
      setTimeout(() => successMsg.remove(), 500);
    }, 5000);
  }
})();
