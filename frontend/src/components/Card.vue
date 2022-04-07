<template>
  <div>
    <b-col>
       <div v-if="type==='drivers'">
        <driver-card :deleteFunction="deleteFunction" :parsedData="parsedData" ></driver-card>
      </div>
      <div v-else-if="type === 'buses'">
        <bus-card :parsedData="parsedData"  :deleteFunction="deleteFunction" ></bus-card>
      </div>
      <div v-else-if="type === 'journeys'">
        <journey-card :parsedData="parsedData" ></journey-card>
      </div>
      <div  v-else-if="type === 'passengers'">
        <passenger-card :parsedData="parsedData"></passenger-card>
      </div> 

    </b-col>
  </div>
</template>

<script>
import BusCardVue from './cardContents/BusCard.vue';
import DriverCard from "./cardContents/DriverCard.vue"
import JourneyCard from "./cardContents/JourneyCard.vue"
import PassengerCard from "./cardContents/Passenger.vue"

export default {
  props: ["data","type", "id"],
  components: {
    "driver-card": DriverCard, "bus-card": BusCardVue,
    "journey-card": JourneyCard, "passenger-card": PassengerCard
  },
  data(){
    return {
      // type: this.type,
      parsedData: { ...this.data }
    }
  },
  methods: {
    deleteFunction(){
      const deleteReq = async() =>{
          let object_ = {...this.parsedData}
          let element_id_key = Object.keys(object_).filter(element => { if(element.indexOf('id')>-1) return element})
          // console.log(this.type, object_[element_id_key])
         console.log("1")
         await this.$store.dispatch("deleteElement", { type: this.type, element_id: object_[element_id_key] });
         console.log("2")
         await this.$store.dispatch("fetchJobs",{ type: this.type });
          console.log("3")
      }

      deleteReq()
    }
  },
  mounted(){
    // this.parsedData=this.parseData
  },
  computed: {
    modalId() {
      return `modal-${this.id}`;
    }
  }

  
};
</script>

<style scoped></style>
