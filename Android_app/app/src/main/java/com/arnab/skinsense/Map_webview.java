package com.arnab.skinsense;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class Map_webview extends AppCompatActivity {
    WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_map_webview);
        webView = findViewById(R.id.webpage_view_map);

        webView.setWebViewClient(new WebViewClient());

        webView.loadUrl("http://192.168.1.26:7000");
    }
}