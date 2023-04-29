package com.example.iotandroidapplication;
import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class ImageClass {

    @SerializedName("prediction")
    @Expose
    private String prediction;

    @SerializedName("type")
    @Expose
    private String type;

    public String getPrediction() {
        return prediction;
    }

    public void setPrediction(String prediction) {
        this.prediction = prediction;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

}