<template>
  <main>
    <div class="about">
      <section id="introduction">
        <h2>Introduction</h2>
        <p>
          The Interactive Lighting Project aims to create an immersive lighting system for gaming rooms, offering users
          interactive options that dynamically change lighting effects based on reactive sound or user control. The
          lighting setup, which can be mounted on a Velcro panel, provides versatility in placement near a power outlet.
          This README provides an extensive overview of the project's objectives, technical details, and an installation
          guide.
        </p>
      </section>

      <section id="projectGoals">
        <h2>Project Goals</h2>
        <p>
          The primary objective of this project is to develop a customizable and expandable lighting system for gaming
          rooms. The system should enrich gaming experiences by responding to in-game sounds in real-time, allowing
          users to interact with the lighting in various ways and adjust colors and patterns to match their preferences.
        </p>
      </section>

      <section id="features">
        <h2>introduction</h2>
        <ul class="list">
          <li>User-Controlled Lighting: The lighting system enables users to interact with it via a webpage, offering
            flexibility in customization.</li>
          <li>Customizable Settings: Users can adjust lighting colors, brightness, and patterns to create their desired
            gaming atmosphere.</li>
          <li>Reactive Audio support: With the installation of a seperate program one can even use their computers
            audiostream to control the leds.</li>
          <li>Effortless adjustment: Because the LED strips are stuck to the panel with velcro, you can easily adjust
            the position of every individual LED strip segment. This makes sure that the user can place them where
            he/she sees fit.</li>
        </ul>
      </section>

      <section id="webpage">
        <h2>Webpage</h2>
        <p>
          A website has been developed to provide full control over the lights. It features different sections for LED
          control such as color, brightness adjustment, on/off control (Home page), effect selection (Effects page), and
          information about the project (About page).
        </p>
        <br>

        <h2>Home Page</h2>
        <p>
          This page allows control of the general LED settings. Users can adjust the solid color, brightness, and turn
          the lights on or off. There's a left side with a color picker and buttons for predefined colors, and a right
          side with controls for power and brightness, as well as a button for random effects.
        </p>
        <br>

        <h2>Effect Page</h2>
        <p>
          Here, users can choose from a variety of effects available in WLED. They can either search for specific
          effects or browse through the entire list to select one, enabling them to create a unique gaming atmosphere.
        </p>
        <br>

        <h2>About Page</h2>
        <p>
          This page provides detailed information about the project's goals, features, and technical specifications.
          It's intended for informational purposes only and does not offer LED control.
        </p>
      </section>

      <hr id="line">

      <section id="github">
        <p>For more information go to our github</p>
        <button id="githubButton"><a href="https://github.com/vives-project-xp/InteractiveLighting" id="githubButtonlink" target="_blank">GitHub</a></button>
      </section>
    </div>
  </main>
</template>

<style>
body {
  background-color: #000f2c;
  color: wheat;
  font-size: medium;
  justify-content: center;
  background-image: url("../assets/Images/image.png");
  background-size: 100vh;
  background-repeat: no-repeat;
  background-position: center;
  background-attachment: fixed;
}

main{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.about {
  width: 60%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  align-self: center;
}

.list{
  list-style-type: none;
  justify-items: left;
}

#githubButtonlink{
  text-decoration: none;
  color: black;
}

#githubButton {
  width: 100%;
  background-color: rgb(155, 208, 183);
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  border: none;
}

#githubButton:hover {
  background-color: rgb(217, 151, 116);
  transition: 1000ms;
}

#githubButton:active {
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.2);
  transform: translateY(1px);
}

#line{
  width: 100%;
  direction: horizontal;
  border: 3px solid wheat;
  color: wheat;
}

/* ------ Custom Scrollbar ------ */

/* Define the scrollbar style */
::-webkit-scrollbar {
  -webkit-appearance: none;
  appearance: none;
  width: 15px;
  height: 15px;
}

/* Define the thumb style */
::-webkit-scrollbar-thumb {
  -webkit-appearance: none;
  appearance: none;
  background-color: wheat;
  border-radius: 7px;
}

/* Define the track style */
::-webkit-scrollbar-track {
  -webkit-appearance: none;
  appearance: none;
  background-color: transparent;
}
</style>
