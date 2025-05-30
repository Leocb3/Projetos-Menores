package br.uniceub.cc.pdm.base64;

import android.os.Bundle;
import android.util.Base64;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private EditText inputText;
    private TextView resultText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputText = findViewById(R.id.inputText);
        resultText = findViewById(R.id.resultText);

        Button buttonEncode = findViewById(R.id.buttonEncode);
        Button buttonDecode = findViewById(R.id.buttonDecode);

        buttonEncode.setOnClickListener(this::encodeToBase64);
        buttonDecode.setOnClickListener(this::decodeFromBase64);
    }

    private void encodeToBase64(View view) {
        String text = inputText.getText().toString();
        String encoded = Base64.encodeToString(text.getBytes(), Base64.DEFAULT);
        resultText.setText("Base64: " + encoded);
    }

    private void decodeFromBase64(View view) {
        String encodedText = inputText.getText().toString();
        try {
            byte[] decodedBytes = Base64.decode(encodedText, Base64.DEFAULT);
            String decoded = new String(decodedBytes);
            resultText.setText("Texto: " + decoded);
        } catch (IllegalArgumentException e) {
            resultText.setText("Texto inválido para decodificação.");
        }
    }
}
