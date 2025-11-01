from huggingface_hub import snapshot_download

cache_dir = "models/cache"

######### Models #########
# save_dir = "models/BAGEL-7B-MoT"
# repo_id = "ByteDance-Seed/BAGEL-7B-MoT"
# snapshot_download(cache_dir=cache_dir,
#   local_dir=save_dir,
#   repo_id=repo_id,
#   local_dir_use_symlinks=False,
#   resume_download=True,
#   allow_patterns=["*.json", "*.safetensors", "*.bin", "*.py", "*.md", "*.txt"],
# )


save_dir = "src/open-r1-multimodal/data/Data-DeQA-Score"
repo_id = "zhiyuanyou/Data-DeQA-Score"
snapshot_download(cache_dir=cache_dir,
  local_dir=save_dir,
  repo_id=repo_id,
  local_dir_use_symlinks=False,
  resume_download=True,
  repo_type="dataset",
)
# cd src/open-r1-multimodal/data/Data-DeQA-Score/KONIQ
# wget -c http://datasets.vqa.mmsp-kn.de/archives/koniq10k_1024x768.zip


# git clone https://www.modelscope.cn/datasets/zhiyuanyou/DataDepictQA.git
save_dir = "src/open-r1-multimodal/data/DataDepictQA"
repo_id = "zhiyuanyou/DataDepictQA"
snapshot_download(cache_dir=cache_dir,
  local_dir=save_dir,
  repo_id=repo_id,
  local_dir_use_symlinks=False,
  resume_download=True,
  repo_type="dataset",
)
