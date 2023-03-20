# tts_fastspeech2
基于fastspeech2模型，使用标贝数据集进行训练的中文语音合成系统，包含前端demo（使用django实现）

## dataset
- [标贝数据集](https://www.data-baker.com/data/index/TNtts)

## processe data
使用 [MFA](https://mfa-models.readthedocs.io/en/latest/index.html) 进行数据预处理，过程参考 [Montreal Forced Aligner使用教程（中文语音文本对齐）](https://zhuanlan.zhihu.com/p/613596010)
所使用的 [声学模型和字典](https://pan.baidu.com/s/14tqUZZ-0vLOTaeaVmFAt-A?pwd=mma3#list/path=%2F) 提取码：mma3

## References
- [FastSpeech 2: Fast and High-Quality End-to-End Text to Speech](https://arxiv.org/abs/2006.04558), Y. Ren, *et al*.
- [FastSpeech 2 - PyTorch Implementation](https://github.com/ming024/FastSpeech2), Chien Chung-Ming, *et al*.