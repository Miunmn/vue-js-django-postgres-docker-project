
<template>
      <b-card
        :title="`${this.parsedData.first_name} ${this.parsedData.last_name}`"
        img-src="https://previews.123rf.com/images/dolgachov/dolgachov1901/dolgachov190100734/115184774-group-of-happy-passengers-travelling-by-bus.jpg"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem;"
        class="mb-2"
      >
        <b-card-text>
          Trayecto id: {{parsedData.assigned_journey_id}}
        </b-card-text>
      </b-card>
</template>

<script>
    export default{
        props: ["parsedData"]

    }

</script>