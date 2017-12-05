<!-- 
#
#	David Meyer
#	dmm@1-4-5.net
#	Fri Jul 21 08:33:24 2000
#
#	$Header: /mnt/disk0/dmm/public_html/ml/RCS/index.html,v 1.19 2017/09/15 19:26:01 dmm Exp $
#
-->

<HEAD>
<LINK REV=MADE HREF=mailto:dmm@1-4-5.net>


<h2>
Random (and largely incomplete) thoughts/snippets on various ML topics
</h2>

<!-- 
<center>
<img src="./bp.jpg" style="width:444px;height:368px;">
</center>
-->

<h2>Thoughts</h2>
<ul>

<li><a href="./trpo.pdf">Notes on Policy Gradients (Trust Region Policy Optimization, under construction)</li>
<li><a href="./pg.pdf">Notes on Policy Gradients (under construction)</li>
<li><a href="./nce.pdf">Notes on Noise Contrastive Estimation (NCE)</li>
<li><a href="./sgn.pdf">Notes on Maximization of Inner Products over Norm Balls</li>
<li><a href="./adversarial.pdf">Notes on Adversarial Examples</li>
<li><a href="./ps.pdf">Basic probability stuff that everyone likely should know</li>
<li><a href="./vae.pdf">Notes on Variational Autoencoders </li>
<li><a href="./log_derivative_trick.pdf">Notes on policy gradient
and the log derivative trick for reinforcement learning (under construction)</li>
<li><a href="./lda_intro.pdf">LDA Intro/overview (also under construction)</li>
<li><a href="./ae.pdf">Brief intro to auto-encoders (I would explain this differently/use different notation these days)</li>
<li><a href="./cp.pdf">Pretty old random idea</li>
<li><a href="./how_does_word2vec_work.pdf">How exactly does word2vec work?</li>
<li><a href="./mm.pdf">Why is minimizing error the same thing as
maximizing likelihood is the same thing as finding a low energy state...</li>
<li><a href="./seq2seq.pdf">A bit on sequence to sequence learning (e.g Google Inbox smart reply)</a></li>
</ul>

<h2>Code Snippets</h2>
<ul>
<li><a
href="https://github.com/davidmeyer/ml/tree/master/tensorflow">VariationalAutoencoder</a>
(VAE) and other examples written in tensorflow. An example
reconstruction of MNIST digits by the VAE is shown below.</li>
<a href="https://github.com/davidmeyer/ml/blob/master/tensorflow/variational_autoencoder.ipynb"><img src="./images/training_epochs.png" style="width:300px;height:250px;"></a>.

<li><a href="code/lr.py">lr.py: </a>Very simple linear regression in
tensorflow (made up dataset)</li>
<img src="./images/lr.png" style="width:350px;height:250px;">


<li><a href="code/k-prototypes.py">k-prototypes.py:</a> Categorical
Clustering for Netflow data</li>
<li><a href="code/mnist_softmax_regression.py">Softmax regression</a> on
<a href="http://yann.lecun.com/exdb/mnist/">MNIST</a> in tensorflow</li>
<li><a href="code/pca+km.scala">PCA + K-Means</a>
(Spark/MLlib/Scala) on the <a
href="http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html">KDDCUP99
data set </a></li>
</ul>

<br>
<br>
<hr>
<i>Last Update: 2017.09.15 by <a href=mailto:dmm@1-4-5.net>dmm@1-4-5.net</a>
</i>
<br>
</BODY>
</HTML>

