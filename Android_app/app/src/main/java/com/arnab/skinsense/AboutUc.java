package com.arnab.skinsense;

import android.app.Fragment;
import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

/**
 * Created by User on 20-03-2018.
 */

public class AboutUc extends android.support.v4.app.Fragment implements View.OnClickListener
{
    ImageView bhrt, har, sid, bhrtin, harin, sidin;
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.about,null);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        bhrt = view.findViewById(R.id.bhrt);
        har = view.findViewById(R.id.har);
        sid = view.findViewById(R.id.sid);
        bhrtin = view.findViewById(R.id.bhrtin);
        harin = view.findViewById(R.id.harin);
        sidin = view.findViewById(R.id.sidin);


        bhrt.setOnClickListener(this);
        har.setOnClickListener(this);
        sid.setOnClickListener(this);
        bhrtin.setOnClickListener(this);
        harin.setOnClickListener(this);
        sidin.setOnClickListener(this);
    }

    @Override
    public void onClick(View view){
        Intent i = new Intent(view.getContext(), WebViewActivity.class);
        switch(view.getId()){
            case R.id.bhrt:{
                i.putExtra("link", "http://192.168.1.26:7007");
                break;
            }
            case R.id.har:{
                i.putExtra("link", "https://github.com/Ravanv2");
                break;
            }
            case R.id.sid:{
                i.putExtra("link", "https://github.com/sidoff8");
                break;
            }

            case R.id.bhrtin:{
                i.putExtra("link", "https://www.linkedin.com/in/bhrt-sharma/");
                break;
            }
            case R.id.harin:{
                i.putExtra("link", "https://www.linkedin.com/in//");
                break;
            }
            case R.id.sidin:{
                i.putExtra("link", "https://www.linkedin.com/in/sidharth1806/");
                break;
            }

        }
        startActivity(i);
    }
}
