<template>
  <main>
  <div class="about">
    <h1 class="AboutH1">About Interactive Lighting Project</h1>
    <h2>How does it work?</h2>
    <br />
    <p>
      We use multiple led strips that are connected to the gaming setup and
      these will project different lighting paterns depending on what sound is
      made in the game you're playing.
    </p>
    <p></p>
    <section id="introduction">
      <h2>Introduction</h2>
      <p>
        Welcome to the Interactive Lighting project overview! Our team was
        tasked with creating an immersive lighting system for a gaming room,
        offering users various interaction options that dynamically alter the
        lighting patterns based on in-game actions and ambient sound.
      </p>
    </section>

    <section id="goal">
      <h2>What's Our Goal?</h2>
      <p>
        We were given the task to create lighting for a gaming room that users
        can interact with in different ways, affecting the coloring and pattern
        of the lighting. Our primary goal is to transform a standard gaming room
        into an immersive and dynamic space using interactive LED strips.
        Situated within our school premises, this project aims to create an
        engaging environment where students can enjoy gaming experiences
        enhanced by responsive lighting. By integrating interactive LED
        technology, we aspire to elevate the gaming room into an innovative hub
        that not only entertains but also inspires creativity and collaboration
        among students."
      </p>
    </section>

    <section id="how-it-works">
      <h2>How Does It Work?</h2>
      <p>
        We use multiple LED strips connected to the gaming setup, which project
        different lighting patterns depending on the in-game sound.
      </p>
    </section>

    <section id="features">
      <h2>Features</h2>
      
          Real-time Responsiveness: The lighting system reacts instantly to
          in-game events and ambient sound, providing a seamless and immersive
          experience.
        
    </section>

    <section id="expandability">
      <h2>Expandability</h2>
      <p>
        This project has been designed with expandability in mind, allowing for
        future enhancements and additions without significant rework.
      </p>
    </section>

    <section id="software">
      <h2>Software We Used</h2>
      <div>
        <ul id="list">
          <li>Arduino</li>
          <li>WLED</li>
          <li>Fusion 360</li>
        </ul>
      </div>
    </section>

    <section id="hardware">
      <h2>Hardware We Used</h2>
      <ul id="list">
        <li>ESP32</li>
        <li>24V Power Supply</li>
        <li>DC/DC Converter</li>
        <li>WS2812 LED Strips</li>
        <li>
          Ceiling Mounting Hardware (later replaced with a panel and velcro)
        </li>
        <li>JST Connectors</li>
        <li>Velcro</li>
      </ul>
    </section>

    <section id="changes">
      <h2>Changes During the Project</h2>
      <p>
        Originally, we planned to mount the LED strips on the ceiling, but later
        decided to stick them to a panel with velcro for easier installation and
        flexibility.
      </p>
    </section>
  </div>
  </main>
</template>

<style>
body {
  background-color: #000f2c;
  color: wheat;
  
  justify-content: center;
  background-image: url("../assets/Images/image.png");
  background-size: 100vh;
  background-repeat: no-repeat;
  background-position: center;
  background-attachment: fixed;
}

#list{
  align-items: center;
  justify-content: center;
}


.about{
  padding-left: 20px;
  text-align: left;
}

.AboutH1{
  
  font-size: 3em; 
  color: rgb(223, 201, 160);
  text-align: center;
  text-shadow: 5px 5px 20px wheat, -5px -5px 20px wheat}
</style>
