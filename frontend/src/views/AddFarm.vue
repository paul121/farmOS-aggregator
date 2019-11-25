<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="ma-3">
            <v-toolbar dark color="primary">
              <v-toolbar-title class="headline">Add a farm</v-toolbar-title>
            </v-toolbar>

            <v-form v-model="valid" ref="form" lazy-validation>

              <v-card-text>
                <div class="subtitle-1 text--primary">
                  Add your farm to the {{appName}}. Your farm will appear on the {{appName}} map!
                </div>
                <br>
                <div class="headline text--primary">
                  Farm Info
                </div>

                <v-text-field label="Farm Name" v-model="farmName" required></v-text-field>
                <v-text-field label="URL" v-model="url" required></v-text-field>
                <v-text-field label="Notes (Optional)" v-model="notes"></v-text-field>
                <v-text-field label="Tags (Optional)" v-model="tags"></v-text-field>

              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="cancel">Cancel</v-btn>
                <v-btn @click="reset">Reset</v-btn>
                <v-btn
                        @click="submit"
                        :disabled="!valid"
                >
                  Save
                </v-btn>
              </v-card-actions>


            </v-form>

          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import { Store } from 'vuex';
import { IUserProfileUpdate } from '@/interfaces';
import { appName } from '@/env';
import { commitAddNotification } from '@/store/main/mutations';
import { dispatchResetPassword } from '@/store/main/actions';

@Component
export default class UserProfileEdit extends Vue {
  public appName = appName;
  public valid = true;
  public password1 = '';
  public password2 = '';

  public mounted() {
    this.checkToken();
  }

  public reset() {
    this.password1 = '';
    this.password2 = '';
    this.$validator.reset();
  }

  public cancel() {
    this.$router.push('/');
  }

  public checkToken() {
    const token = (this.$router.currentRoute.query.token as string);
    if (!token) {
      commitAddNotification(this.$store, {
        content: 'No token provided in the URL, start a new password recovery',
        color: 'error',
      });
      this.$router.push('/recover-password');
    } else {
      return token;
    }
  }

  public async submit() {
    if (await this.$validator.validateAll()) {
      const token = this.checkToken();
      if (token) {
        await dispatchResetPassword(this.$store, { token, password: this.password1 });
        this.$router.push('/');
      }
    }
  }
}
</script>
