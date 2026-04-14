<template>
    <div class="container mt-4"> <!--Looks neater-->


    <h2 class="mb-2">Upload Form</h2>

    <p v-if="message" :class="status">
    {{ message }}
    </p>

    
     <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
      
      <!-- Title -->
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input 
          type="text" 
          name="title" 
          class="form-control"
          v-model="title"
        />
      </div>

      <!-- Description -->
      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea
            name="description"
            class="form-control"
            v-model="description"
            rows="4"
        ></textarea> <!--Fixed this to allow for bigger text box-->
      </div>

      <!-- Poster -->
      <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster</label>
        <input 
          type="file" 
          name="poster" 
          class="form-control"
          @change="handleFileUpload"
        />
      </div>

      <!-- Submit Button -->
      <button type="submit" class="btn btn-primary">
        Save Movie
      </button>



    </form>

    </div>

   

</template>


<script setup>
import { ref , onMounted } from 'vue'


const title = ref('')
const description = ref('')
const poster = ref(null)
const message = ref('')

const status = ref('success')

const csrf_token = ref("")


function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then(response => response.json())
    .then(data => {
      console.log(data)
      csrf_token.value = data.csrf_token
    })
} 

onMounted(() => {
  getCsrfToken()
})

function handleFileUpload(event) {
  poster.value = event.target.files[0]
}

function saveMovie() {

  let movieForm = document.getElementById('movieForm')
  let form_data = new FormData(movieForm)

  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      "X-CSRFToken": csrf_token.value
    }
  })
    .then(response => {
    if (!response.ok) {
        return response.json().then(error => {
        throw error
        })
    }
    return response.json()
    })
    .then(data => {
    console.log(data)

    status.value = "success"
    message.value = "Movie uploaded successfully!"

    title.value = ""
    description.value = ""
    poster.value = null
    })
    .catch(error => {
    console.log(error)

    status.value = "error"

    message.value = error.error || "Error uploading movie"
    })
}

</script>

<style scoped>

.success { 
    border: 1px solid green;
    background-color: lightgreen; 
    border-radius: 5px;
    padding: 12px;
    margin-top: 10px;

}
.error { 
    border: 1px solid red;
    background-color: lightcoral; 
    border-radius: 5px;
    padding: 12px;
    margin-top: 10px;
    }
</style>