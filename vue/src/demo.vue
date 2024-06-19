<template>
  <div>
    <el-button type="success">Success Button</el-button>
    <el-input v-model="inputValue" placeholder="Enter something"></el-input>
    <p>You entered: {{ inputValue }}</p>
    <p>You return data: {{ returnvalue }}</p>
    <el-button type="primary" @click="sendData">Send Data</el-button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Demo',
  data() {
    return {
      inputValue: '',
	  returnvalue:''
    }
  },
  methods: {
    async sendData() {
      try {
        const response = await axios.post('api/test', {
          data: this.inputValue
        })
        console.log('Data sent successfully:', response.data)
		this.returnvalue = response.data
      } catch (error) {
        console.error('Error sending data:', error)
      }
    }
  }
}
</script>

