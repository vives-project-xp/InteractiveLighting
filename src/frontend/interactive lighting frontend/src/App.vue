<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>
<template>
  <nav class="navbar navbar-expand-lg" id="fullNavbar">
    <div class="container-fluid">
      <a
        class="navbar-brand"
        id="navbarnolink"
        href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        target="_blank"
        >Interactive lighting</a>
      <div id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <RouterLink to="/">Home</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/Effect">Effect</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/About">About</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <RouterView />
</template>

<style scoped>
body {
  line-height: 1.5;
  max-height: 100vh;
  max-width: 100vw;
  font-size: 1vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 2vh;
  margin-top: 2rem;
  background-color: rgb(155, 208, 183);
  color: black;
  border-radius: 2cap;
  box-shadow: 5px 5px 20px rgba(155, 208, 183, 0.8),
    -5px -5px 20px rgba(171, 185, 179, 0.8);
}

nav a:first-of-type {
  border: 0;
  color: black;
}

nav a.router-link-exact-active {
  color: rgb(25, 63, 157);
}

.nav-item:hover {
  background-color: rgba(88, 86, 86, 0.597);
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid white;
}

#navbarnolink {
  background-color: transparent;
}
</style>
