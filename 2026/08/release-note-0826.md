
# Title: August 25, 2026 
Link: https://docs.cloud.google.com/release-notes#August_25_2026<br>
Google Cloudインフラエンジニアとして、リリースノートに基づいた調査結果を以下にご報告いたします。

---

# Cloud SDK
## Breaking
原文: (なし)
説明：今回のリリースノートでは、Cloud SDKの「Breaking Change」（互換性のない変更）カテゴリが記載されていますが、具体的な変更内容や詳細は提供されていません。
影響有無：このリリースノート自体には具体的な変更内容が記載されていないため、現時点での直接的な影響はありません。しかし、「Breaking」カテゴリが存在することから、Cloud SDKの今後のリリースで既存の構成やスクリプトに影響を与える非互換の変更が導入される可能性があることを示唆しています。
対処方法：現時点での具体的な対処は不要です。ただし、Cloud SDKの今後のバージョンアップ時には、リリースノートを注意深く確認し、もし「Breaking Change」が導入された場合は、既存のアプリケーションや自動化スクリプトへの影響を評価し、必要に応じて改修を計画してください。
用語説明：
*   **Cloud SDK**: Google Cloudのリソースやサービスをコマンドラインから操作するためのツールセットです。`gcloud`コマンドなどが含まれます。
*   **Breaking Change**: ソフトウェアの新しいバージョンがリリースされた際に、既存のアプリケーションやシステムが以前のバージョンで動作していたようには動作しなくなる、互換性のない変更を指します。これにはAPIの変更、デフォルト設定の変更、機能の削除などが含まれることがあります。

---

# Google Kubernetes Engine
## Fixed
原文:
Fixed the issue in which GPUDirect-TCPX for `a3-highgpu-8g` machine types was
incompatible with the Linux kernel version that was used by Container-Optimized
OS in GKE version 1.34 and later. To prevent errors, GKE blocked creating or
upgrading node pools that used the `a3-highgpu-8g` machine type to version 1.34
and later. For more information about this issue, see GKE known
issues.

[GKE known
issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/known-issues#tcpx-cos125)
You can now create or upgrade node pools that use the `a3-highgpu-8g` machine
type to any of the following GKE versions. **Automatic upgrades of these node
pools from version 1.33 to version 1.34 or later are no longer blocked.**

- For minor version 1.34, use patch version 1.34.5-gke.1153000 or later.
- For minor version 1.35, use patch version 1.35.2-gke.1485000 or later.
- For minor version 1.36 and later, use any available patch version.

In GKE version 1.34 and later, you must use version 3.1.9 or later of the
GPUDirect-TCPX installer and version 2.0.12 or later of the GPUDirect-TCPX
sidecar. If you previously installed these components, verify that the container
images use these versions or later. **To avoid degraded performance or workload
failures, update your installer and sidecar image versions before the
`a3-highgpu-8g` node pools are manually or automatically upgraded to version
1.34 or later.** These container image versions correspond to the upstream
definitions maintained in the gpudirect-tcpx GitHub
repository.

[gpudirect-tcpx GitHub
repository](https://github.com/GoogleCloudPlatform/container-engine-accelerators/tree/master/gpudirect-tcpx)

説明：Google Kubernetes Engine (GKE) において、`a3-highgpu-8g` マシンタイプでGPUDirect-TCPXを使用する際に、GKEバージョン1.34以降のContainer-Optimized OS (COS) のLinuxカーネルバージョンとの非互換性があった問題が修正されました。この問題のため、以前は`a3-highgpu-8g`ノードプールをGKE 1.34以降に作成またはアップグレードすることがブロックされていました。
今回の修正により、特定のGKEパッチバージョン（1.34.5-gke.1153000以降、1.35.2-gke.1485000以降など）を使用することで、このブロックが解除され、`a3-highgpu-8g`ノードプールのバージョン1.33から1.34以降への自動アップグレードも再開されます。
**重要事項として、GKEバージョン1.34以降では、GPUDirect-TCPXインストーラーとGPUDirect-TCPXサイドカーのバージョンをそれぞれ3.1.9以降、2.0.12以降に更新する必要があります。** これらのコンポーネントが古いバージョンのままだと、パフォーマンスの低下やワークロードの障害が発生する可能性があります。

影響有無：
*   **影響あり（正の影響）**:
    *   現在`a3-highgpu-8g`マシンタイプを使用しており、GPUDirect-TCPXを利用しているGKEクラスターでは、これまでブロックされていたGKEバージョン1.34以降へのアップグレードが可能になります。
    *   バージョン1.33から1.34以降への自動アップグレードがブロックされなくなり、クラスタの自動メンテナンスが再開されます。
*   **影響あり（要対応）**:
    *   `a3-highgpu-8g`マシンタイプを使用し、GPUDirect-TCPXを利用しているGKEクラスターをバージョン1.34以降にアップグレードする前に、GPUDirect-TCPXインストーラーのコンテナイメージをバージョン3.1.9以降、GPUDirect-TCPXサイドカーのコンテナイメージをバージョン2.0.12以降に更新する必要があります。これを怠ると、パフォーマンスが低下したり、ワークロードが失敗する可能性があります。
*   **影響なし**:
    *   `a3-highgpu-8g`マシンタイプやGPUDirect-TCPXを使用していないGKEクラスターには直接的な影響はありません。

対処方法：
1.  **影響範囲の確認**: ご利用のGKEクラスターが`a3-highgpu-8g`マシンタイプを使用しており、GPUDirect-TCPXを利用しているかを確認してください。
2.  **対象となる場合**:
    *   **GPUDirect-TCPXコンポーネントのバージョン確認と更新**: GKEのバージョンを1.34以降にアップグレードする前に、現在デプロイされているGPUDirect-TCPXインストーラーとサイドカーのコンテナイメージのバージョンが、それぞれ3.1.9以降および2.0.12以降であることを確認してください。もし古いバージョンを使用している場合は、[gpudirect-tcpx GitHub repository](https://github.com/GoogleCloudPlatform/container-engine-accelerators/tree/master/gpudirect-tcpx)を参照し、最新の推奨バージョンに更新してください。
    *   **GKEのアップグレード計画**: 必要なGPUDirect-TCPXコンポーネントのバージョンアップが完了した後、GKEクラスターを影響のないパッチバージョン（例: 1.34.5-gke.1153000以降、1.35.2-gke.1485000以降）へアップグレードする計画を立ててください。自動アップグレードが再開されるため、アップグレード前にワークロードの互換性テストと十分な準備を行うことを推奨します。
用語説明：
*   **Google Kubernetes Engine (GKE)**: Google Cloudが提供するマネージドなKubernetesサービスで、コンテナ化されたアプリケーションのデプロイ、管理、スケーリングを容易にします。
*   **`a3-highgpu-8g` マシンタイプ**: Google CloudのA3 VMインスタンスシリーズの一つで、特に高性能なNVIDIA H100 GPUを8基搭載しており、大規模なAI/ML（機械学習）ワークロードやHPC（高性能計算）に最適化されています。
*   **GPUDirect-TCPX**: NVIDIAが提供する技術で、GPUとネットワークインターフェースカード（NIC）間のデータ転送をCPUを介さずに直接行うことで、高スループットと低レイテンシを実現します。主に高性能なGPUクラスタ間通信で利用されます。
*   **Container-Optimized OS (COS)**: Googleが提供する、コンテナ実行に特化して最適化されたLinuxベースのオペレーティングシステムです。GKEノードのデフォルトOSとして広く利用されています。
*   **ノードプール**: GKEクラスタ内で、同じ設定（マシンタイプ、OSイメージなど）を持つVMインスタンス（ノード）のグループです。
*   **サイドカー**: コンテナ化されたアプリケーションの設計パターンの一つで、メインのアプリケーションコンテナと同じPod内で補助的な機能を提供する別のコンテナを実行するものです。ここではGPUDirect-TCPXの機能を提供するコンテナを指します。