from flask import Flask, render_template_string, send_file
import os

app = Flask(__name__)

# قائمة الصور
images = [
    'https://telegra.ph/file/cedd72b1855f33a6f4f02.jpg',
    'https://telegra.ph/file/a6693cefdeda75546151e.jpg',
    'https://telegra.ph/file/c9d3f4e00cfc687494989.jpg',
    'https://telegra.ph/file/e98e8e77cab37b038c2fe.jpg', 'https://telegra.ph/file/eb9685d19b680de308c6d.jpg',
    'https://telegra.ph/file/6607e95bb8ee17fc33881.jpg', 'https://telegra.ph/file/ceca65f3cb13b2e452d03.jpg',
    'https://telegra.ph/file/a82aca5b0b274b8757ffa.jpg', 'https://telegra.ph/file/cec3728a7101198bf13a8.jpg',
    'https://telegra.ph/file/24a17c37570cdebb0c205.jpg', 'https://telegra.ph/file/0f6a669c76afbe4f65bdd.jpg',
    'https://telegra.ph/file/7fb966a620c8f46ad8414.jpg', 'https://telegra.ph/file/df45047d5400f55a9ef1c.jpg',
    'https://telegra.ph/file/34bf4d46aa11ba1eb4494.jpg', 'https://telegra.ph/file/a879ac10a6c6dcc568d7a.jpg',
    'https://telegra.ph/file/1c6011439ea2cd749caec.jpg', 'https://telegra.ph/file/c2e8ce01bff924749df8b.jpg',
    'https://telegra.ph/file/396159fa48ef6bfae0061.jpg', 'https://telegra.ph/file/c271e9ae20c6e711d6c49.jpg',
    'https://telegra.ph/file/45e92514780f3e4c9623a.jpg', 'https://telegra.ph/file/cd26c2eb4e53acc52ca81.jpg',
    'https://telegra.ph/file/457330c8488d21bb269bb.jpg', 'https://telegra.ph/file/c5da67e6ba44414e4f6c0.jpg',
    'https://telegra.ph/file/c0b72b8fb3337e9122800.jpg', 'https://telegra.ph/file/ff7345f942d71d59bb02b.jpg',
    'https://telegra.ph/file/e340747d0becad1d61d15.jpg', 'https://telegra.ph/file/6fc3c134cdd36659b7ffc.jpg',
    'https://telegra.ph/file/aedd1a6aa5ebf32a30116.jpg', 'https://telegra.ph/file/cd7360a8d5ef454a9be26.jpg',
    'https://telegra.ph/file/cef7fccedc623420bc2ba.jpg', 'https://telegra.ph/file/73cfc13e082b2df13c159.jpg',
    'https://telegra.ph/file/0f29961f1a1f7529450a2.jpg', 'https://telegra.ph/file/07c3f5a543f7b4680fd57.jpg',
    'https://telegra.ph/file/400821f43ba3a7b6119a0.jpg', 'https://telegra.ph/file/5867d14be9bbc7a41cba0.jpg',
    'https://telegra.ph/file/76dd4ef3232bc7bab13c6.jpg', 'https://telegra.ph/file/1a3ab5a862149fc5b8d19.jpg',
    'https://telegra.ph/file/4f0784d7b562da987d4bf.jpg', 'https://telegra.ph/file/2a7127a33af65e119c7f7.jpg',
    'https://telegra.ph/file/3dee97df8a07ac46fdc28.jpg', 'https://telegra.ph/file/772c4ce47adf6b0a24816.jpg',
    'https://telegra.ph/file/e7d990a1140208ccca08c.jpg', 'https://telegra.ph/file/9f7df26326092a1c97a39.jpg',
    'https://telegra.ph/file/40c018a92e4ed4180affc.jpg', 'https://telegra.ph/file/386df51d24abe0c2b9f9d.jpg',
    'https://telegra.ph/file/6f7c9b78b8a88e6449f75.jpg', 'https://telegra.ph/file/f2ba56e55a69427c3863c.jpg',
    'https://telegra.ph/file/21ab1f8120efda42a8a9e.jpg', 'https://telegra.ph/file/6f322e7fd5073a7130ae0.jpg',
    'https://telegra.ph/file/b09f58d7e177c3b31ea0b.jpg', 'https://telegra.ph/file/cf1a34c452e1964a28b6e.jpg',
    'https://telegra.ph/file/4ffeecdab62d0d9816e24.jpg', 'https://telegra.ph/file/190f97acf242648b5a787.jpg',
    'https://telegra.ph/file/a392e3d2a7fb7555c41b4.jpg', 'https://telegra.ph/file/0e769d48fdd5fead5ba8e.jpg',
    'https://telegra.ph/file/4f32ac91ee36ce20d0534.jpg', 'https://telegra.ph/file/e6d8bf7ee12306e8f204e.jpg',
    'https://telegra.ph/file/1e30ca64ef58a350e24b5.jpg', 'https://telegra.ph/file/fdd1292660d3ebc6e732d.jpg',
    'https://telegra.ph/file/03de8281dbd4b72cacd17.jpg', 'https://telegra.ph/file/71dba29677d49882292db.jpg',
    'https://telegra.ph/file/4805b03b59e90d8bbd81e.jpg', 'https://telegra.ph/file/9caa9dbd705ed4a631d26.jpg',
    'https://telegra.ph/file/6e428264a7ab2163b566e.jpg', 'https://telegra.ph/file/62e46e1a2f2e585bca90d.jpg',
    'https://telegra.ph/file/c112e1eff65d2a003cb79.jpg', 'https://telegra.ph/file/d5153cb89555641527b08.jpg',
    'https://telegra.ph/file/00e597dd228a86bcade46.jpg', 'https://telegra.ph/file/80531535ea19ab389458c.jpg',
    'https://telegra.ph/file/a1bb47296cd5ffddbbd19.jpg', 'https://telegra.ph/file/59e5a8d4a0fba29a9fd37.jpg',
    'https://telegra.ph/file/f189a39b9a960c8ef0959.jpg', 'https://telegra.ph/file/60c1ff83551d3dccc8fe3.jpg',
    'https://telegra.ph/file/e3687548d0798d8d726fc.jpg', 'https://telegra.ph/file/2806166c3b8870da30732.gif',
    'https://telegra.ph/file/7995757d0486981a9119c.jpg', 'https://telegra.ph/file/1e9b7c320ec2ab9d7dc2b.jpg',
    'https://telegra.ph/file/91363d547936d19034fee.jpg', 'https://telegra.ph/file/015d6c21c3f4c5750a64e.jpg',
    'https://telegra.ph/file/96eb7d72c2d040543882b.jpg', 'https://telegra.ph/file/575c5a36060d49187d202.jpg',
    'https://telegra.ph/file/9b592a74a93c20bf31673.jpg', 'https://telegra.ph/file/7a63a024fa6aec4e9fa04.jpg',
    'https://telegra.ph/file/a9614cb9cde742578fd5b.jpg', 'https://telegra.ph/file/ba2194d597141865cb567.jpg',
    'https://telegra.ph/file/d5b80b73ed4d5b9880119.jpg', 'https://telegra.ph/file/294b1e140cdd5dd1b9f1d.jpg',
    'https://telegra.ph/file/ff92afd7217c0b6d3b4b6.jpg', 'https://telegra.ph/file/92393603d519d775e0e92.jpg',
    'https://telegra.ph/file/df831b0e7421c881f24b7.jpg', 'https://telegra.ph/file/6e80f67b1ffe2d3c71534.jpg',
    'https://telegra.ph/file/17541812699a76bd29f3c.jpg', 'https://telegra.ph/file/2dc30d61c58f0c25f8c38.jpg',
    'https://telegra.ph/file/2a48cd00d4c54ee051f4d.jpg', 'https://telegra.ph/file/9ad06848d0f9869539c2a.jpg',
    'https://telegra.ph/file/f0d25d7d3883d7011b4bd.jpg', 'https://telegra.ph/file/f48ba0bfa6f148a204bd7.jpg',
    'https://telegra.ph/file/28e877fc428cc80b16eae.jpg', 'https://telegra.ph/file/305df5ab0cc3fa329e210.jpg',
    'https://telegra.ph/file/dd9a6250cd1f279cb20ac.jpg', 'https://telegra.ph/file/20551ba08cbe5c1f9f448.jpg',
    'https://telegra.ph/file/6401168d9808d7e425be4.jpg', 'https://telegra.ph/file/2fcf5d242c879aac5e0da.jpg',
    'https://telegra.ph/file/1ff8d6a7384650503c509.jpg', 'https://telegra.ph/file/0ba450b8060c9ae2a980d.jpg',
    'https://telegra.ph/file/8721d59f6c25090e86074.jpg', 'https://telegra.ph/file/c831dd78b2db4ab62ab98.jpg',
    'https://telegra.ph/file/7f9928ea4b86e02b5f745.jpg', 'https://telegra.ph/file/b769e3a3e83f983ba4ef2.jpg',
    'https://telegra.ph/file/c198a9904a8ad13487428.jpg', 'https://telegra.ph/file/0bdbbb83c7d04c4c31b29.gif',
    'https://telegra.ph/file/9fac4060868d95f745962.jpg', 'https://telegra.ph/file/c172d401fb5acf4c4a7d6.jpg',
    'https://telegra.ph/file/0643aab86b61d67888c77.jpg', 'https://telegra.ph/file/ad1f793ec83a8f577cab1.jpg',
    'https://telegra.ph/file/84ca14386fbf0ec0ea086.jpg', 'https://telegra.ph/file/ff6490688560af9dc4730.jpg',
    'https://telegra.ph/file/5b600dd5db3fcd6d25596.jpg', 'https://telegra.ph/file/261fd992cd33e6fe18721.jpg',
    'https://telegra.ph/file/4392792482ee486386369.jpg', 'https://telegra.ph/file/68b0ef2cbb3bd69cbe0bb.jpg',
    'https://telegra.ph/file/c6f29d0dd90e7f852ac2c.jpg', 'https://telegra.ph/file/955fa54e7d1a97d15a250.jpg',
    'https://telegra.ph/file/80ef3f2defc48cc3bc9ae.jpg', 'https://telegra.ph/file/8b9f19c8020313da34b96.jpg',
    'https://telegra.ph/file/f7865bb630627c0292798.jpg', 'https://telegra.ph/file/cf403595221953210ab03.jpg',
    'https://telegra.ph/file/aa5774932a177d97780e3.jpg', 'https://telegra.ph/file/fbf337d764ed306c632d3.jpg',
    'https://telegra.ph/file/a9ac847973421986267b4.jpg', 'https://telegra.ph/file/38d0bd880825e682c22e2.jpg',
    'https://telegra.ph/file/e169d6019ae5b3547d9c3.jpg', 'https://telegra.ph/file/80a509d1901f0a01dcf8b.jpg',
    'https://telegra.ph/file/7903fe2f220357325d2c7.jpg', 'https://telegra.ph/file/f1881bfdd315c7d251ed9.jpg',
    'https://telegra.ph/file/ef58e1cc30f41d5d1c1c1.jpg', 'https://telegra.ph/file/2d0fce623e69600009f30.jpg',
    'https://telegra.ph/file/2bfb8c65713e011bb56c9.jpg', 'https://telegra.ph/file/0bd5820855fe4f347ed02.jpg',
    'https://telegra.ph/file/341cd38f33c97128221be.jpg', 'https://telegra.ph/file/e437e4cb52782152924ae.jpg',
    'https://telegra.ph/file/c784fc4f0fd35b3860355.jpg', 'https://telegra.ph/file/83202dd156724f0e807df.jpg',
    'https://telegra.ph/file/446befb2e190d706dce23.jpg', 'https://telegra.ph/file/8536ac9aa314b875ac340.jpg',
    'https://telegra.ph/file/0988a94845dbc4e8ad471.jpg', 'https://telegra.ph/file/cbd588d96a5388da4c783.jpg',
    'https://telegra.ph/file/717f80065572ff5ebcfe4.jpg',
    'https://telegra.ph/file/31a524f90ce386ac54872.jpg',
    'https://telegra.ph/file/e40b00a747c14d5938b39.jpg',
    'https://telegra.ph/file/b7552a3422cf224450934.jpg',
    'https://telegra.ph/file/8b2bc593e96d208329bc6.jpg',
    'https://telegra.ph/file/d7382bebc1c817bf6746e.jpg',
    'https://telegra.ph/file/4a4d5cec019ac9db437f7.jpg',
    'https://telegra.ph/file/36aa017f69952521bc146.jpg',
    'https://telegra.ph/file/31dbd693bc4a8744e0e1a.jpg',
    'https://telegra.ph/file/d6a50e01dc355c973056a.jpg',
    'https://telegra.ph/file/114ffa86272e3ce8227b8.jpg',
    'https://telegra.ph/file/259f4e38d7e3a50ef818f.jpg',
    'https://telegra.ph/file/582d698a9f2757ed1a7ca.jpg',
    'https://telegra.ph/file/d223e5715938d9836d239.jpg',
    'https://telegra.ph/file/75d19710475b100da9fd1.jpg',
    'https://telegra.ph/file/ad520db9a31531f799806.jpg',
    'https://telegra.ph/file/b861203929e1c24807858.jpg',
    'https://telegra.ph/file/34871a29b87a7d28f9cc7.jpg',
    'https://telegra.ph/file/8f4572ee159fb0e5dbe3e.jpg',
    'https://telegra.ph/file/383f755d059888017c41c.jpg',
    'https://telegra.ph/file/3e3b212bb9fce4e8ebee4.jpg',
    'https://telegra.ph/file/381e46ae0394a9a5f6c3e.jpg',
    'https://telegra.ph/file/5001ba33cbadf30812039.jpg',
    'https://telegra.ph/file/0eddaf721639a12ac4b65.jpg',
    'https://telegra.ph/file/b2b227aef17032e5d9512.jpg',
    'https://telegra.ph/file/b871d94064830fa1d7b3f.jpg',
    'https://telegra.ph/file/3d59d74add04df0472c64.jpg',
    'https://telegra.ph/file/812707f875430ef7e6642.jpg',
    'https://telegra.ph/file/624a4401df603605a4eb4.jpg',
    'https://telegra.ph/file/8d8edb73228bd68cf7c4d.jpg',
    'https://telegra.ph/file/93bb658d674fcbabf4fc4.jpg',
    'https://telegra.ph/file/6dafddc93645d6a5aa7da.jpg',
    'https://telegra.ph/file/fcd6a40f4e4bfe87add36.jpg',
    'https://telegra.ph/file/93418de858750285eb5b3.jpg',
    'https://telegra.ph/file/9233a59f07397d761cbdf.jpg',
    'https://telegra.ph/file/963b283e7e0c028d03400.jpg',
    'https://telegra.ph/file/a2eb57a427199e898f7b3.jpg',
    'https://telegra.ph/file/0e8dcdab1c26c9035e927.jpg',
    'https://telegra.ph/file/e01fca538d005681f1aaf.jpg',
    'https://telegra.ph/file/9e3e8158ac5ddb6402e29.jpg',
    'https://telegra.ph/file/fd8f4f83ab8199cdf3fbb.jpg',
    'https://telegra.ph/file/10979a90e8511fd5ee666.jpg',
    'https://telegra.ph/file/bbc784647e3b8a94ae7a8.jpg',
    'https://telegra.ph/file/9a45d72ed8cc4f6f6f5cf.jpg',
    'https://telegra.ph/file/4a161e63b5b2d52df6a7b.jpg',
    'https://telegra.ph/file/2a6d3f1f0ea8259c09cf6.jpg',
    'https://telegra.ph/file/ecbc6864c8f80d43ac4bb.jpg',
    'https://telegra.ph/file/e1bbac099b50f3fd116f6.jpg',
    'https://telegra.ph/file/05c43b86a62b6a76891b3.jpg',
    'https://telegra.ph/file/67f9b5494e14baa43edf5.jpg',
    'https://telegra.ph/file/e490a33b24dec410ffb82.jpg',
    'https://telegra.ph/file/dc4750d193128b27596be.jpg',
    'https://telegra.ph/file/bb3cb9095897e06a809c9.jpg',
    'https://telegra.ph/file/a3f7bbe91ad822e6323bf.jpg',
    'https://telegra.ph/file/9abe3defc2ced7379d9b1.jpg',
    'https://telegra.ph/file/a3dba3f5d99a192924c76.jpg',
    'https://telegra.ph/file/f21c7cfb726e6ab0c18f3.jpg',
    'https://telegra.ph/file/b4bc39bb7c6a2fc9344e0.jpg',
    'https://telegra.ph/file/f151e267a73728d222063.jpg',
    'https://telegra.ph/file/b6d44b48bd440b39c0384.jpg',
    'https://telegra.ph/file/b5562d3d572dec825e5ad.jpg',
    'https://telegra.ph/file/cd37de1807fe1dca47cbc.jpg',
    'https://telegra.ph/file/611a2a9df1971b7870b69.jpg',
    'https://telegra.ph/file/18066bcd9b29c3042b59c.jpg',
    'https://telegra.ph/file/9a81f43809a53c4c511ca.jpg',
    'https://telegra.ph/file/bd2bac84370eda813d4cf.jpg',
    'https://telegra.ph/file/ac0563cc4c2f46ad562a8.jpg',
    'https://telegra.ph/file/f82353cabd254b9f666ed.jpg',
    'https://telegra.ph/file/3e2d46a7365654a198c6d.jpg',
    'https://telegra.ph/file/5e50b0f2cee03f92f1d7f.jpg',
    'https://telegra.ph/file/fa0ab7fa14c6ed38edb65.jpg',
    'https://telegra.ph/file/0c7fed9c2b57fac02edc7.jpg',
    'https://telegra.ph/file/285d8b9536d2f0a141e7d.jpg',
    'https://telegra.ph/file/88d10e904ef7b1182b91f.jpg',
    'https://telegra.ph/file/29bdd0317fa50cb8c92b1.jpg',
    'https://telegra.ph/file/fa886bdc11e3b648adc8b.jpg',
    'https://telegra.ph/file/15eba80b374bb3bd6fc67.jpg',
    'https://telegra.ph/file/ae87357b9f063b2b35d2b.jpg',
    'https://telegra.ph/file/65dd762be3a46bdec6805.jpg',
    'https://telegra.ph/file/632bc2b0509c666d658ac.jpg',
    'https://telegra.ph/file/86a197856bfd5c4fb8c2e.jpg',
    'https://telegra.ph/file/f2df20786971f60d667a6.jpg',
    'https://telegra.ph/file/27f3a4f7cd9c8bfd9ce3d.jpg',
    'https://telegra.ph/file/f61d21414e81e51feb38e.jpg',
    'https://telegra.ph/file/81c62486f06b8be2bcf31.jpg',
    'https://telegra.ph/file/87301aee9ac00653d902f.jpg',
    'https://telegra.ph/file/ecd4d092a02c72a1a2f4f.jpg',
    'https://telegra.ph/file/a7e18af41e529bd8fe0cb.jpg',
    'https://telegra.ph/file/58e5a4cfe4850e727fc6d.jpg',
    'https://telegra.ph/file/f2a0f24df7e3ac5565369.jpg',
    'https://telegra.ph/file/1ad2b6f2ed7b0afe2e7e5.jpg',
    'https://telegra.ph/file/6b39c261e655019d70edf.jpg',
    'https://telegra.ph/file/71c7e45680a729d4e6b52.jpg',
    'https://telegra.ph/file/2c36ab729b0ed7b66a6c4.jpg',
    'https://telegra.ph/file/d918bcbab3a2199df052c.jpg',
    'https://telegra.ph/file/1c08d0ffdc57f5bd46080.jpg',
    'https://telegra.ph/file/2aea254af4a1e5fb6d637.jpg',
    'https://telegra.ph/file/e2701ded833917bad31c4.jpg',
    'https://telegra.ph/file/41f365808b986477130fb.jpg',
    'https://telegra.ph/file/d97873df8502a02c876ec.jpg',
    'https://telegra.ph/file/3fd8d4aef7baa6dbc9e11.jpg',
    'https://telegra.ph/file/5cb9bcada1f12990f1889.jpg',
    'https://telegra.ph/file/b958f971e4b364a5b479e.jpg',
    'https://telegra.ph/file/9a98ae082ccad1b0adac4.jpg',
    'https://telegra.ph/file/7aa44747ba8bf02b985ab.jpg',
    'https://telegra.ph/file/97715a76f5925ac6663cc.jpg',
    'https://telegra.ph/file/2512ffe6e690b44b439a6.jpg',
    'https://telegra.ph/file/943b9b84499f4595eed4a.jpg',
    'https://telegra.ph/file/513c2dbed550b415e952e.jpg',
    'https://telegra.ph/file/620ad41213afd5f7a2aa0.jpg',
    'https://telegra.ph/file/45818aba62f60fee1875a.jpg',
    'https://telegra.ph/file/88d37b3404c78b105caa7.jpg',
    'https://telegra.ph/file/75ab7e25527d1f8553080.jpg',
    'https://telegra.ph/file/40bbfd4958ae8d4b6d965.jpg',
    'https://telegra.ph/file/5299c8b00fc0e0bc7cb5a.jpg',
    'https://telegra.ph/file/8e61403490c57a4727206.jpg',
    'https://telegra.ph/file/0953797a3275bcb9ede50.jpg',
    'https://telegra.ph/file/94b4518d5e56402fe159a.jpg',
    'https://telegra.ph/file/54db5f482756b9c8045bf.jpg',
    'https://telegra.ph/file/e29ea5645d017e86626b0.jpg',
    'https://telegra.ph/file/83e3c82348c320157051e.jpg',
    'https://telegra.ph/file/c77428a9893bb129c1b10.jpg',
    'https://telegra.ph/file/896f1fdf49d6c864e6af0.jpg',
    'https://telegra.ph/file/01e31d5c9a044196b3ce9.jpg',
    'https://telegra.ph/file/405692d75b79fd24fcd20.jpg',
    'https://telegra.ph/file/363a1a4ae1874adabcfe7.jpg',
    'https://telegra.ph/file/44f616eca735264afda80.jpg',
    'https://telegra.ph/file/2857a3e97b84e103cd4fa.jpg',
    'https://telegra.ph/file/4f1b295c7d100b4dbae39.jpg',
    'https://telegra.ph/file/65df527f5181c0f668650.jpg',
    'https://telegra.ph/file/722a29e505fc9f8a43f82.jpg',
    'https://telegra.ph/file/dcf457c4d16ffcca100c6.jpg',
    'https://telegra.ph/file/b0db26b7be7a3c34f4bb0.jpg',
    'https://telegra.ph/file/bdccbbfdf9e5dc2d445bf.jpg',
    'https://telegra.ph/file/5b3bbbbc621cd4d2746b7.jpg',
    'https://telegra.ph/file/566695a1ea48e61027819.jpg',
    'https://telegra.ph/file/b37909ed34b94c7c09fcb.jpg',
    'https://telegra.ph/file/f913f7cc801257020f857.jpg',
    'https://telegra.ph/file/ee9ae7e62030deb61a7b8.jpg',
    'https://telegra.ph/file/0f1b41538db503ca9dddf.jpg',
    'https://telegra.ph/file/7acc3cadc8b0b1bc4a4f7.jpg',
    'https://telegra.ph/file/0c6db7e5247c27aa539d6.jpg',
    'https://telegra.ph/file/8bde19341f9440cee4829.jpg',
    'https://telegra.ph/file/207b7cc6a5b89d7921a52.jpg',
    'https://telegra.ph/file/21ee87c2c9b702cf80da7.jpg',
    'https://telegra.ph/file/7d4b91037be73164194af.jpg',
    'https://telegra.ph/file/89dc441cbb96d5311b318.jpg',
    'https://telegra.ph/file/198e92c493c55e1b3ba3c.jpg',
    'https://telegra.ph/file/776160976fb61d43c1fdb.jpg',
    'https://telegra.ph/file/d323a911442b954aa5469.jpg',
    'https://telegra.ph/file/cb631388aec7202ec0539.jpg',
    'https://telegra.ph/file/07537cb43374cfe6a7acf.jpg',
    'https://telegra.ph/file/cfe5bc210705d421df8a5.jpg',
    'https://telegra.ph/file/cb7f13b5ab24bcfa5bdae.jpg',
    'https://telegra.ph/file/4f101c8b1c0a5a79b63a1.jpg',
    'https://telegra.ph/file/de0963e7dbef135cb9158.jpg',
    'https://telegra.ph/file/988bba0e26c500f5e40e5.jpg',
    'https://telegra.ph/file/f4d11a83ce2df589254be.jpg',
    'https://telegra.ph/file/385dd115b628caef4a568.jpg',
    'https://telegra.ph/file/39eb8cd60bba16c681d17.jpg',
    'https://telegra.ph/file/d1292750eaa197603ae12.jpg',
    'https://telegra.ph/file/c663b5d1ffc0cb7210292.jpg',
    'https://telegra.ph/file/6d452b7a14994c810bc1f.jpg',
    'https://telegra.ph/file/941af8cb730ff4597301d.jpg',
    'https://telegra.ph/file/d53b1a0cc6310405fb4df.jpg',
    'https://telegra.ph/file/06047f102a4f379d43f93.jpg',
    'https://telegra.ph/file/dfa37fd0f842f10cf0df5.jpg',
    'https://telegra.ph/file/781ed7b452227807a952a.jpg',
    'https://telegra.ph/file/08d43ebdf596418d7e7c3.jpg',
    'https://telegra.ph/file/b90b180b97650b3b2c543.jpg',
    'https://telegra.ph/file/b0e27aef5f5b05677f93d.jpg',
    'https://telegra.ph/file/79340b2973b7d15ab8c6c.jpg',
    'https://telegra.ph/file/353e648223a33a14f1a08.jpg',
    'https://telegra.ph/file/e2d19866bfa9b4d35a533.jpg',
    'https://telegra.ph/file/bd83ad9f0c11ebb4ea83c.jpg',
    'https://telegra.ph/file/2310ea596c69d8d55ee39.jpg',
    'https://telegra.ph/file/1586d0ad53f5774763d1b.jpg',
    'https://telegra.ph/file/e9de87e8121ca640f0bdb.jpg',
    'https://telegra.ph/file/7760fdc6a673bb6ea435c.jpg',
    'https://telegra.ph/file/c3640a8406ca8938e05d1.jpg',
    'https://telegra.ph/file/945d35d1e89395cb54667.jpg',
    'https://telegra.ph/file/5150719aad06d41f84a2e.jpg',
    'https://telegra.ph/file/fc5ade816b02491143ff1.jpg',
    'https://telegra.ph/file/28c425b1e82d0b44d5d65.jpg',
    'https://telegra.ph/file/7ad5e2a3b99ad4312b598.jpg',
    'https://telegra.ph/file/f3e0016835bde77cfff79.jpg',
    'https://telegra.ph/file/f1026853f1aa4bc487571.jpg',
    'https://telegra.ph/file/c00f8819882c5b66b1c0b.jpg',
    'https://telegra.ph/file/d143d1156043eb67190a4.jpg',
    'https://telegra.ph/file/19f361230d16b2788cc3c.jpg',
    'https://telegra.ph/file/6c8aac8c73d742b6bac3f.jpg',
    'https://telegra.ph/file/94c9eda6a1ab70d3ad524.jpg',
    'https://telegra.ph/file/3b6fe7a17753036fb5e40.jpg',
    'https://telegra.ph/file/b343983ffb41914907822.jpg',
    'https://telegra.ph/file/d51f56d8529257a89c2d4.jpg',
    'https://telegra.ph/file/862f434816e7a65bd2064.jpg',
    'https://telegra.ph/file/4883905c6e1244d14a018.jpg',
    'https://telegra.ph/file/9485f47daa7f11004689c.jpg',
    'https://telegra.ph/file/3e839c78c1548bd2a3d37.jpg',
    'https://telegra.ph/file/9c7a968d66c8838eeadcb.jpg',
    'https://telegra.ph/file/ef0a7a4ab935aca51d92a.jpg',
    'https://telegra.ph/file/0bb14d92552e80acb6a71.jpg',
    'https://telegra.ph/file/6c4f08344109b7dab8ef2.jpg',
    'https://telegra.ph/file/6b3433f35d3364c29522c.jpg',
    'https://telegra.ph/file/22e3239eb343ccf7cfeb0.jpg',
    'https://telegra.ph/file/e2c0fff072b5ea9949d1f.jpg',
    'https://telegra.ph/file/03633cf0b2cc8f21af935.jpg',
    'https://telegra.ph/file/17242135a825478606d1b.jpg',
    'https://telegra.ph/file/3e9b0048f19dfc5faff9c.jpg',
    'https://telegra.ph/file/17de4dedcc2991629487e.jpg',
    'https://telegra.ph/file/022a53b2b701e47682e41.jpg',
    'https://telegra.ph/file/0f2ed9aebdf37062f58e0.jpg',
    'https://telegra.ph/file/82b5bb380c94aa69eeec4.jpg',
    'https://telegra.ph/file/5eef9c4110175bc19837c.jpg',
    'https://telegra.ph/file/d9321df00524b2843e64b.jpg',
    'https://telegra.ph/file/eab78cb3852aa6f53d5a4.jpg',
    'https://telegra.ph/file/7157056e5f773184b1e7e.jpg',
    'https://telegra.ph/file/9c66b18696d3a40278a62.jpg',
    'https://telegra.ph/file/015341ad87a0a058ce9ca.jpg',
    'https://telegra.ph/file/3a1edf38ab9c9d5ab71af.jpg',
    'https://telegra.ph/file/f4f8eb86501919f1f150e.jpg',
    'https://telegra.ph/file/75f5a0dcece137308d2ec.jpg',
    'https://telegra.ph/file/1b90da7c82735b4969b8d.jpg',
    'https://telegra.ph/file/fcdab98db8c89c67d1429.jpg',
    'https://telegra.ph/file/1ec08b0fd46d955779002.jpg',
    'https://telegra.ph/file/fbdcdc48dab4c5b3cc872.jpg',
    'https://telegra.ph/file/ae2eae0e9d89991101e70.jpg',
    'https://telegra.ph/file/e808ade992cba63103676.jpg',
    'https://telegra.ph/file/a4cf5541f5487df24aba4.jpg',
    'https://telegra.ph/file/00ed4405fe4adc870faf7.jpg',
    'https://telegra.ph/file/3cd0400a5ae311417e9b4.jpg',
    'https://telegra.ph/file/145296a4fb3fb2973dc33.jpg',
    'https://telegra.ph/file/75627390c4e55c0049731.jpg',
    'https://telegra.ph/file/c6afcff1a6e647f22a9a6.jpg',
    'https://telegra.ph/file/e63bcd925ebe90243663a.jpg',
    'https://telegra.ph/file/12a700140fa59574938bb.jpg',
    'https://telegra.ph/file/1e1c0a7459ef9c7aca0fa.jpg',
    'https://telegra.ph/file/3d7ed50775a4be24727b2.jpg',
    'https://telegra.ph/file/b67b518d0052c7e52656f.jpg',
    'https://telegra.ph/file/563a008c6ff42142e3bab.jpg',
    'https://telegra.ph/file/5d33848ecda00ef2d93f2.jpg',
    'https://telegra.ph/file/342778e2cfa533155766d.jpg',
    'https://telegra.ph/file/b94d445aedf2c2889daa7.jpg',
    'https://telegra.ph/file/a1a01a94c395e4cf15c2b.jpg',
    'https://telegra.ph/file/76273a0f0823a99c5496e.jpg',
    'https://telegra.ph/file/b657895985048c357886f.jpg',
    'https://telegra.ph/file/55782007d4f521f2bea07.jpg',
    'https://telegra.ph/file/cb1351c2d5b707b661950.jpg',
    'https://telegra.ph/file/de39730dd3ff347074f45.jpg',
    'https://telegra.ph/file/8c2880323a6502c53acd1.jpg',
    'https://telegra.ph/file/ec80b0580babd0cacecf3.jpg',
    'https://telegra.ph/file/6e64570d070457b3e320b.jpg',
    'https://telegra.ph/file/d1f99a97fa4dd1bd68dc8.jpg',
    'https://telegra.ph/file/6dda43cd06f6789bbe4fb.jpg',
    'https://telegra.ph/file/9d6446ed28ed0a70e9fd5.jpg',
    'https://telegra.ph/file/ff734579e407365fba75f.jpg',
    'https://telegra.ph/file/5ce3fa6bdd4cfe6f0833a.jpg',
    'https://telegra.ph/file/32a135247e13586608dac.jpg',
    'https://telegra.ph/file/cad9d09841b4d57ff7abc.jpg',
    'https://telegra.ph/file/bc34493587a99159f403e.jpg',
    'https://telegra.ph/file/55bfc6244e1a2ce041c68.jpg',
    'https://telegra.ph/file/e35bb5e27ca950a3462a9.jpg',
    'https://telegra.ph/file/b671e859119a337058e51.jpg',
    'https://telegra.ph/file/83ea3b81178ddc2f45b29.jpg',
    'https://telegra.ph/file/8c2ce8d61cf49cde19678.jpg',
    'https://telegra.ph/file/44f65124d878085982a6d.jpg',
    'https://telegra.ph/file/53fc755590f59a419b673.jpg',
    'https://telegra.ph/file/a72945e3b869e748cc5aa.jpg',
    'https://telegra.ph/file/60b56db8526f2334c547b.jpg',
    'https://telegra.ph/file/627abfe344e80798d215b.jpg',
    'https://telegra.ph/file/326dc9734f0266a236dd5.jpg',
    'https://telegra.ph/file/62e11d9792fc7ef8bc690.jpg',
    'https://telegra.ph/file/092a1e27ee2d5c1b19fb0.jpg',
    'https://telegra.ph/file/5995235036ab33355bf16.jpg',
    'https://telegra.ph/file/f4041927ef5ea73d80532.jpg',
    'https://telegra.ph/file/a30973b5fecfd1b7621d1.jpg',
    'https://telegra.ph/file/a423fd0860d48da6a041f.jpg',
    'https://telegra.ph/file/de28eee190ce8759ec245.jpg',
    'https://telegra.ph/file/7c2735350d2a8fad3d61b.jpg',
    'https://telegra.ph/file/a28d869cf9bf4721cb2d9.jpg',
    'https://telegra.ph/file/e9b3c548e1a28cafccd2b.jpg',
    'https://telegra.ph/file/758d120ce43c064e13f52.jpg',
    'https://telegra.ph/file/e589e1ba7e6aee6dde203.jpg',
    'https://telegra.ph/file/4e5141e8f53f99ce55363.jpg',
    'https://telegra.ph/file/8785db1fab74cb7be6976.jpg',
    'https://telegra.ph/file/a9a540ccbae98dec56a68.jpg',
    'https://telegra.ph/file/b4c853afb2b54dd0e92af.jpg',
    'https://telegra.ph/file/ae63cb885008d3350d4ce.jpg',
    'https://telegra.ph/file/e9291b15d5d54c775bec3.jpg',
    'https://telegra.ph/file/8a26da727288557868462.jpg',
    'https://telegra.ph/file/db696bb673d74a984a5c5.jpg',
    'https://telegra.ph/file/c7ee9c7956c8825acfdb8.jpg',
    'https://telegra.ph/file/dc65567d812887b2e2a12.jpg',
    'https://telegra.ph/file/bf6520c126a579ba11b82.jpg',
    'https://telegra.ph/file/9daeb7e71bdd787cd4e13.jpg',
    'https://telegra.ph/file/4a6ed57569f84aaeba137.jpg',
    'https://telegra.ph/file/5be66f91fdd2693fb0350.jpg',
    'https://telegra.ph/file/bd468e26df5a69df8bba8.jpg',
    'https://telegra.ph/file/95fda121a3fa16f30e2e8.jpg',
    'https://telegra.ph/file/e57aab6cb71f9e4132678.jpg',
    'https://telegra.ph/file/e37ff23531ed20d83db0d.jpg',
    'https://telegra.ph/file/bc1633381a5eb289f5e0d.jpg',
    'https://telegra.ph/file/d10ff6a3a9883af6967b0.jpg',
    'https://telegra.ph/file/5f62d4bbb8107829fb08d.jpg',
    'https://telegra.ph/file/ebe9b16bd016ab120b499.jpg',
    'https://telegra.ph/file/7e68654462b36bb1a00fd.jpg',
    'https://telegra.ph/file/8cdce882390b1364d8d9f.jpg',
    'https://telegra.ph/file/01ad244bd4642104c080d.jpg',
    'https://telegra.ph/file/1c230d4d49e5f00b613ee.jpg',
    'https://telegra.ph/file/44fe7ba6b9838d0608b77.jpg',
    'https://telegra.ph/file/0ddc5100f10e6d0006dc3.jpg',
    'https://telegra.ph/file/ecabb2acb84606eacf147.jpg',
    'https://telegra.ph/file/3e0050ee09165b8018dc7.jpg',
    'https://telegra.ph/file/25a7ab121b25e3f61f15e.jpg',
    'https://telegra.ph/file/6ccdbd6c451852f71b7ab.jpg',
    'https://telegra.ph/file/c4bec153276ef2698a332.jpg',
    'https://telegra.ph/file/8977a65d31ce5ca90fa65.jpg',
    'https://telegra.ph/file/0ace038d9ca103b363a63.jpg',
    'https://telegra.ph/file/682f14ead6f93bf2936e9.jpg',
    'https://telegra.ph/file/38584023ec08a246d457f.jpg',
    'https://telegra.ph/file/860f9018e96217537549b.jpg',
    'https://telegra.ph/file/73aca177289d8f8b6998e.jpg',
    'https://telegra.ph/file/712206af4d7297a29edfd.jpg',
    'https://telegra.ph/file/83e984cae5366d5836878.jpg',
    'https://telegra.ph/file/c7db3f1f8b113da295c54.jpg',
    'https://telegra.ph/file/cbbb07820b670d692924b.jpg',
    'https://telegra.ph/file/589d976d445733a0eb58c.jpg',
    'https://telegra.ph/file/0dcac47c37221a3ca6695.jpg',
    'https://telegra.ph/file/e4580e17d3ac3e3be852c.jpg',
    'https://telegra.ph/file/9ce9b32863f0b467f0c6a.jpg',
    'https://telegra.ph/file/ad65822d57cb1b680f37c.jpg',
    'https://telegra.ph/file/77d3cdb745b6c1b4ee1a0.jpg',
    'https://telegra.ph/file/674506a5159503c5cd8a0.jpg',
    'https://telegra.ph/file/1e0372ff378da94a56016.jpg',
    'https://telegra.ph/file/59ab84954c9cfa49ef6bc.jpg',
    'https://telegra.ph/file/412d20a654eccd1f75031.jpg',
    'https://telegra.ph/file/fe72b55220984373f42a6.jpg',
    'https://telegra.ph/file/a85f890b419a98bf3f155.jpg',
    'https://telegra.ph/file/e54a3521a351cf7b59631.jpg',
    'https://telegra.ph/file/fbae1bfaac517fcb21129.jpg',
    'https://telegra.ph/file/8e91880025b9a32630809.jpg',
    'https://telegra.ph/file/837954f721f3c1d926fb3.jpg',
    'https://telegra.ph/file/7ba21978a46f187bd531c.jpg',
    'https://telegra.ph/file/2ed058765d37cab0096e1.jpg',
    'https://telegra.ph/file/7ce3df7d8152db4594a93.jpg',
    'https://telegra.ph/file/d8b9338e712c4a95ef2ee.jpg',
    'https://telegra.ph/file/c09d719215145e8db1e75.jpg',
]
# قائمة الصور المقبولة
accepted_images = []

# المؤشر الحالي للصورة
current_image_index = 0

@app.route('/')
def index():
    global current_image_index
    if current_image_index >= len(images):
        return render_template_string("""
            <html>
                <head>
                    <title>تم عرض كل الصور</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            background-color: #f4f4f4;
                            text-align: center;
                            padding: 50px;
                        }
                        h1 {
                            color: #333;
                        }
                        .container {
                            position: relative;
                            padding: 10px;
                        }
                        .btn {
                            background-color: #4CAF50;
                            color: white;
                            font-size: 18px;
                            padding: 15px 32px;
                            cursor: pointer;
                            border: none;
                            border-radius: 5px;
                            transition: background-color 0.3s;
                        }
                        .btn:hover {
                            background-color: #45a049;
                        }
                    </style>
                </head>
                <body>
                    <h1>تم عرض كل الصور!</h1>
                    <p>لقد قمت بمراجعة كل الصور.</p>
                    <br><br>
                    <a href="/" class="btn">العودة إلى البداية</a>
                </body>
            </html>
        """)

    return render_template_string("""
        <html>
            <head>
                <title>عرض الصورة</title>
                <style>
                    body {
                        font-family: 'Arial', sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #282c34;
                        color: white;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        overflow: hidden;
                    }
                    img {
                        max-width: 90%;
                        max-height: 90%;
                        object-fit: contain;
                        border-radius: 10px;
                        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
                    }
                    .controls {
                        position: absolute;
                        bottom: 50px;
                        width: 100%;
                        display: flex;
                        justify-content: center;
                    }
                    .btn {
                        background-color: #4CAF50;
                        color: white;
                        font-size: 18px;
                        padding: 15px 32px;
                        margin: 0 10px;
                        cursor: pointer;
                        border: none;
                        border-radius: 5px;
                        transition: background-color 0.3s;
                    }
                    .btn:hover {
                        background-color: #45a049;
                    }
                    .top-right {
                        position: absolute;
                        top: 20px;
                        right: 20px;
                        background-color: #007BFF;
                        color: white;
                        padding: 10px 20px;
                        cursor: pointer;
                        border-radius: 5px;
                        text-decoration: none;
                    }
                    .top-right:hover {
                        background-color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <div>
                    <h2>صورة {{ current_image_index + 1 }}</h2>
                    <img src="{{ images[current_image_index] }}" alt="صورة">
                </div>
                <div class="controls">
                    <a href="/accept/{{ current_image_index }}" class="btn">قبول</a>
                    <a href="/reject/{{ current_image_index }}" class="btn">رفض</a>
                </div>
                <a href="/download" class="top-right">تحميل الصور المقبولة</a>
            </body>
        </html>
    """, images=images, current_image_index=current_image_index)

@app.route('/accept/<int:image_index>')
def accept_image(image_index):
    global current_image_index
    if image_index >= 0 and image_index < len(images):
        accepted_images.append(images[image_index])
    current_image_index += 1  # الانتقال للصورة التالية
    return index()

@app.route('/reject/<int:image_index>')
def reject_image(image_index):
    global current_image_index
    current_image_index += 1  # الانتقال للصورة التالية
    return index()

@app.route('/download')
def download_file():
    # قم بإنشاء ملف نصي يحتوي على الصور المقبولة
    file_path = 'accepted_images.txt'
    with open(file_path, 'w') as file:
        for image in accepted_images:
            file.write(image + '\n')

    # تحميل الملف
    return send_file(file_path, as_attachment=True, download_name="accepted_images.txt")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
