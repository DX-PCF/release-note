
# Title: July 20, 2026 
Link: https://docs.cloud.google.com/release-notes#July_20_2026<br>
はい、承知いたしました。Google Cloud のリリースノートを元に、構築済みのサービスへの影響調査結果を製品ごとにご回答します。

---

# Compute Engine

## Deprecated

**原文:** Encrypting disks, snapshots, images, and machine images with customer-supplied encryption keys (CSEKs) is deprecated and will be disabled on July 20, 2027. For more information and alternatives to CSEKs for your Compute Engine resources, see Deprecation of customer-supplied encryption keys (CSEK) in Compute Engine.

**説明:**
Compute Engineのリソース（ディスク、スナップショット、イメージ、マシンイメージ）を、顧客指定の暗号化キー（Customer-Supplied Encryption Keys: CSEK）を使用して暗号化する機能が非推奨化されました。この機能は、2027年7月20日に完全に無効化されます。Googleは、CSEKの代替手段への移行を推奨しています。詳細および代替策については、公式ドキュメント「Compute Engineにおける顧客指定の暗号化キー（CSEK）の非推奨化」を参照してください。

**影響有無:**
*   **影響あり:** 現在、Compute Engineのディスク、スナップショット、イメージ、またはマシンイメージの暗号化にCSEKを利用している場合、影響があります。2027年7月20日以降はCSEKによる暗号化リソースにアクセスできなくなるため、期日までに代替の暗号化方式（例：CMEK）への移行が必要です。
*   **影響なし:** CSEKを利用しておらず、Google管理の暗号化キー（デフォルト）または顧客管理の暗号化キー（CMEK）のみを利用している場合は、直接的な影響はありません。

**対処方法:**
*   **CSEKを利用している場合:**
    *   既存のCSEKで暗号化されたリソースを特定し、2027年7月20日までにGoogle管理の暗号化キーまたは顧客管理の暗号化キー（CMEK）に移行することを検討してください。
    *   移行の具体的な手順については、Google Cloudの公式ドキュメント「[Deprecation of customer-supplied encryption keys (CSEK) in Compute Engine](https://docs.cloud.google.com/compute/docs/deprecations/csek-deprecation-in-compute-engine)」を参照し、適切な移行計画を立ててください。
    *   特に、既存のディスクをCSEKから別の暗号化方式へ移行するには、スナップショットからの新規ディスク作成や、データのエクスポート・インポートなどの手順が必要になる場合があります。

**用語説明:**
*   **Customer-Supplied Encryption Keys (CSEK):** ユーザー自身が生成・管理する暗号化キーをGoogle Cloudに提供し、そのキーを使ってCompute Engineのリソースを暗号化する機能です。キーのライフサイクル管理はユーザーが行う必要があります。
*   **Customer-Managed Encryption Keys (CMEK):** Google Cloud Key Management Service (Cloud KMS) を使用して、ユーザーが暗号化キーの管理（作成、ローテーション、アクセス制御など）を行う機能です。キー自体はCloud KMSに安全に保管され、データの暗号化・復号に使用されます。
*   **Google管理の暗号化キー:** ユーザーが特に設定しなくても、Googleがデフォルトで提供し管理する暗号化キーです。すべての保存データは自動的に暗号化されます。
*   **非推奨化 (Deprecation):** ある機能が将来的に利用できなくなることを事前に通知すること。通常、代替手段が提供され、一定期間の移行猶予が設けられます。

---

# Google Kubernetes Engine

## Deprecated

**原文:** To improve security, Ubuntu node images in GKE version 1.37 and later don't pre-install the `vulkan-tools` package. If you run Vulkan diagnostic tools (such as `vulkaninfo`) directly on GKE Ubuntu hosts, then you must manually install the `vulkan-tools` package. This change doesn't affect containerized GPU/Vulkan workloads.

**説明:**
セキュリティを向上させるため、Google Kubernetes Engine (GKE) のバージョン1.37以降で使用されるUbuntuノードイメージにおいて、`vulkan-tools` パッケージがプリインストールされなくなりました。もし、`vulkaninfo` のようなVulkan診断ツールをGKEのUbuntuホスト上で直接実行する必要がある場合は、手動で `vulkan-tools` パッケージをインストールする必要があります。この変更は、コンテナ化されたGPU/Vulkanワークロードには影響しません。

**影響有無:**
*   **影響あり:** GKEのUbuntuノード上で直接ログインし、`vulkan-tools` パッケージに含まれる診断ツール（例: `vulkaninfo`）を実行している場合に影響があります。GKEのバージョンが1.37以降にアップグレードされると、これらのツールはプリインストールされていないため、手動でのインストールが必要になります。
*   **影響なし:**
    *   GPU/Vulkanを使用するワークロードがコンテナ内部で動作しており、ノードOSに直接依存しない場合、影響はありません。
    *   そもそもVulkanやGPUを使用していない場合、あるいはノード上で直接診断ツールを実行していない場合は影響ありません。
    *   使用しているGKEノードイメージがUbuntu以外（例: Container-Optimized OS）の場合は、この変更の対象外です。

**対処方法:**
*   GKEのUbuntuノード上で `vulkan-tools` が必要な場合は、DaemonSetやSSH経由などで、起動スクリプトや初期化時に手動でパッケージをインストールする手順を追加してください。例えば、`sudo apt-get update && sudo apt-get install -y vulkan-tools` のようなコマンドを実行します。
*   ほとんどのコンテナ化されたGPU/Vulkanワークロードでは、必要なVulkanライブラリやツールはコンテナイメージ内部にバンドルされているため、この変更による追加の対処は不要です。

**用語説明:**
*   **Vulkan:** クロスプラットフォームで高性能なグラフィックスAPI（Application Programming Interface）の一つで、GPUハードウェアへの低レベルなアクセスを提供します。主に3DグラフィックスやGPGPU (General-purpose computing on GPUs) アプリケーションに使用されます。
*   **`vulkan-tools` パッケージ:** Vulkan開発者向けの診断ツールやユーティリティが含まれるパッケージです。例えば `vulkaninfo` は、Vulkan対応のGPUやドライバーに関する詳細情報を表示するツールです。
*   **GPU:** Graphics Processing Unitの略で、グラフィックス処理に特化した演算装置です。深層学習や高性能計算など、並列処理を必要とするワークロードで利用されます。
*   **GKEノードイメージ:** GKEクラスタのワーカーノードで動作するOSイメージです。主にContainer-Optimized OS (COS) やUbuntuが利用されます。
*   **プリインストール:** OSイメージにあらかじめ特定のソフトウェアやパッケージがインストールされている状態を指します。

---