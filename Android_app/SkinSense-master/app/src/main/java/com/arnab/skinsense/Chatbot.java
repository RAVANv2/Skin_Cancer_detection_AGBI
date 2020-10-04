package com.arnab.skinsense;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.KeyEvent;
import android.view.View;
import android.view.inputmethod.EditorInfo;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.util.Log;
import org.json.JSONObject;
import org.json.JSONArray;
import org.json.JSONException;

import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.security.KeyManagementException;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.List;
import java.net.URL;
import java.net.URLConnection;
import java.io.UnsupportedEncodingException;
import android.os.AsyncTask;

import com.google.android.gms.common.GooglePlayServicesNotAvailableException;
import com.google.android.gms.common.GooglePlayServicesRepairableException;
import com.google.android.gms.security.ProviderInstaller;

import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSocketFactory;

public class Chatbot extends AppCompatActivity {

    EditText userInput;
    RecyclerView recyclerView;
    MessageAdapter messageAdapter;
    List<ResponseMessage> responseMessageList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_chatbot);
        
        userInput = findViewById(R.id.userInput);
        recyclerView = findViewById(R.id.conversation);
        responseMessageList = new ArrayList<>();
        messageAdapter = new MessageAdapter(responseMessageList, this);
        recyclerView.setLayoutManager(new LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false));
        recyclerView.setAdapter(messageAdapter);

        userInput.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            @Override
            public boolean onEditorAction(TextView textView, int i, KeyEvent keyEvent) {
                if (i == EditorInfo.IME_ACTION_SEND) {
                    ResponseMessage responseMessage = new ResponseMessage(userInput.getText().toString(), true);
                    responseMessageList.add(responseMessage);
                    RetrieveFeedTask task = new RetrieveFeedTask();
                    task.execute();



                }
                return false;
            }
        });

    }
        // Create GetText Metod
        public void GetText () throws UnsupportedEncodingException {

            String text = "";
            BufferedReader reader = null;

            // Send data
            try {

                // Defined URL  where to send data
                URL url = new URL("https://paidqnabot3.azurewebsites.net/qnamaker/knowledgebases/192e9b82-3d48-4fa2-82c4-587e1ba22351/generateAnswer");
//
//            // Send POST data request
//
                URLConnection conn = url.openConnection();
                conn.setDoOutput(true);
                conn.setDoInput(true);
//
                conn.setRequestProperty("Authorization", "EndpointKey b5ba0699-4c25-416d-8dc9-7448f6e87eb4");
                conn.setRequestProperty("Content-Type", "application/json");

                //Create JSONObject here
                JSONObject jsonParam = new JSONObject();
                String val = userInput.getText().toString();
                ;

                jsonParam.put("question", val);


                OutputStreamWriter wr = new OutputStreamWriter(conn.getOutputStream());
//            wr.write(URLEncoder.encode(jsonParam.toString(), "UTF-8"));
                wr.write(jsonParam.toString());
                wr.flush();
                Log.d("karma", "json is " + jsonParam);

//            // Get the server response

                reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
                Log.d("karma", String.valueOf(reader));
                StringBuilder sb = new StringBuilder();
                String line = null;


                // Read Server Response
                while ((line = reader.readLine()) != null) {
//                 Append server response in string
                    sb.append(line + "\n");
                }

                text = sb.toString();
                JSONObject jsonObj = new JSONObject(text);
                JSONArray answer = jsonObj.getJSONArray("answers");
                JSONObject answer_dict_1 = answer.getJSONObject(0);
                String ans = answer_dict_1.getString("answer");
//            JSONArray answer = answer_dict_1.getJSONArray("answer");

                Log.e("karma", String.valueOf(ans));
                Log.e("karma", String.valueOf(jsonObj));
                ResponseMessage responseMessage2 = new ResponseMessage(ans, false);
                responseMessageList.add(responseMessage2);
                messageAdapter.notifyDataSetChanged();
                if (!isLastVisible())
                    recyclerView.smoothScrollToPosition(messageAdapter.getItemCount() - 1);

                Log.d("karma ", "response is " + text);
            } catch (Exception ex) {
                Log.d("karma", "exception at last " + ex);
            } finally {
                try {

                    reader.close();
                } catch (Exception ex) {
                }
            }
        }


        class RetrieveFeedTask extends AsyncTask<Void, Void, Void> {

            @Override
            protected Void doInBackground(Void... voids) {
                try {
                    Log.d("karma", "called");
                    GetText();
                    Log.d("karma", "after called");

                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                    Log.d("karma", "Exception occurred " + e);
                }

                return null;
            }
        }


    boolean isLastVisible() {
        LinearLayoutManager layoutManager = ((LinearLayoutManager) recyclerView.getLayoutManager());
        int pos = layoutManager.findLastCompletelyVisibleItemPosition();
        int numItems = recyclerView.getAdapter().getItemCount();
        return (pos >= numItems);
    }
}








