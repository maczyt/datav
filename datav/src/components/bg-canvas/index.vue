<template>
  <div style="width:100%;height:100%">
    <canvas id="canv" width="1920" height="572"></canvas>
  </div>
</template>

<script>
import Build from "./build";

export default {
  name: "bg-canvas",
  mounted() {
    const app = new Build();
    app.run();
  }
};
</script>

