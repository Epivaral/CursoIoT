namespace WinformsIoT
{
    partial class ControlarServos
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.lblArriba = new System.Windows.Forms.Label();
            this.Servo = new System.Windows.Forms.TrackBar();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.Servo)).BeginInit();
            this.SuspendLayout();
            // 
            // textBox1
            // 
            this.textBox1.BackColor = System.Drawing.Color.Black;
            this.textBox1.ForeColor = System.Drawing.Color.Lime;
            this.textBox1.Location = new System.Drawing.Point(9, 48);
            this.textBox1.Margin = new System.Windows.Forms.Padding(2);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(314, 187);
            this.textBox1.TabIndex = 1;
            this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.lblArriba);
            this.groupBox2.Controls.Add(this.Servo);
            this.groupBox2.Location = new System.Drawing.Point(327, 48);
            this.groupBox2.Margin = new System.Windows.Forms.Padding(2);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Padding = new System.Windows.Forms.Padding(2);
            this.groupBox2.Size = new System.Drawing.Size(356, 75);
            this.groupBox2.TabIndex = 4;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Servo";
            // 
            // lblArriba
            // 
            this.lblArriba.AutoSize = true;
            this.lblArriba.Location = new System.Drawing.Point(310, 33);
            this.lblArriba.Name = "lblArriba";
            this.lblArriba.Size = new System.Drawing.Size(13, 13);
            this.lblArriba.TabIndex = 1;
            this.lblArriba.Text = "0";
            // 
            // Servo
            // 
            this.Servo.Location = new System.Drawing.Point(16, 24);
            this.Servo.Maximum = 180;
            this.Servo.Name = "Servo";
            this.Servo.Size = new System.Drawing.Size(285, 45);
            this.Servo.TabIndex = 0;
            this.Servo.TickFrequency = 10;
            this.Servo.TickStyle = System.Windows.Forms.TickStyle.Both;
            this.Servo.Scroll += new System.EventHandler(this.Servo_Scroll);
            this.Servo.MouseCaptureChanged += new System.EventHandler(this.Servo_MouseCaptureChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 7.8F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.Color.Red;
            this.label1.Location = new System.Drawing.Point(9, 20);
            this.label1.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(153, 13);
            this.label1.TabIndex = 5;
            this.label1.Text = "Dispositivo desconectado";
            this.label1.Visible = false;
            // 
            // ControlarServos
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(694, 255);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.textBox1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Margin = new System.Windows.Forms.Padding(2);
            this.MaximizeBox = false;
            this.Name = "ControlarServos";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Consola";
            this.Load += new System.EventHandler(this.ControlarServos_Load);
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.Servo)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblArriba;
        private System.Windows.Forms.TrackBar Servo;
    }
}

