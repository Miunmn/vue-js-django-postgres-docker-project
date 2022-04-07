
<template>
      <b-card
        :title="`${this.parsedData.journey_name}`"
        img-src="https://thumbs.dreamstime.com/z/model-travel-bus-map-london-travelling-bus-concept-conceptual-image-travel-tourism-model-travel-bus-108507278.jpg"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem;"
        class="mb-2"
      >
        <b-card-text>
          Origen: {{parsedData.from_city}}
        </b-card-text>
        <b-card-text>
          Destino: {{parsedData.to_city}}
        </b-card-text>
        <b-card-text>
          Fecha: {{date}}
        </b-card-text>
        <b-card-text>
          Bus Id: {{parsedData.assigned_bus_id}}
        </b-card-text>
        <b-card-text>
          Conductor Id: {{parsedData.assigned_driver_id}}
        </b-card-text>


      </b-card>
</template>

<script>
    export default{
        props: ["parsedData"],
        beforeMount(){
          this.parseDate()
        },
        methods: {
          parseDate(){
              let date = new Date(this.parsedData.date)
              var options = {year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
              this.date = date.toLocaleTimeString('es-ES', options)
            }
        },
        
        data(){
            return {
            date: ""
          }
        }
    }

</script>