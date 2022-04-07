<template>
  <div v-if="type==='drivers'">
    <driver-form :type="this.type"></driver-form>
  </div>
  <div v-else-if="type === 'buses'">
    <bus-form :type="this.type"></bus-form>
  </div>
  <div v-else-if="type === 'passengers'">
    <passenger-form :type="this.type"></passenger-form>
  </div>
  <div  v-else-if="type === 'journeys'">
    <journey-form :type="this.type" > </journey-form>
  </div>
</template>

<script>
  import Driver from "./modalContents/DriverModal.vue"
  import Bus from "./modalContents/BusModal.vue"
  import Passenger from "./modalContents/PassengerModal.vue"
  import Journey from "./modalContents/JourneyModal.vue"

  export default {
    props: ["type"],
    components: {
      'driver-form': Driver, 'bus-form': Bus,
      'passenger-form': Passenger, 'journey-form': Journey
    },
    data() {
      return {}
    },
    methods: {

    }
  }
</script>