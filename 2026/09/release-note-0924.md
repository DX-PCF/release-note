
# Title: September 23, 2026 
Link: https://docs.cloud.google.com/release-notes#September_23_2026<br>
Google Cloud のインフラエンジニアとして、ご提示いただいたリリースノートに基づき、構築済みのサービスへの影響有無を調査し、簡潔に回答いたします。

---

# Cloud Service Mesh

## Announcement

### 1.30.4-asm.14 is now available for in-cluster Cloud Service Mesh.
原文: `1.30.4-asm.14 is now available for in-cluster Cloud Service Mesh. For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.30.4-asm.14 uses Envoy v1.38.5-dev.`
説明: Cloud Service Mesh (ASM) の新バージョン 1.30.4-asm.14 が、インクラスターデプロイメント向けにリリースされました。この新しいパッチリリースでは、データプレーンのプロキシとして Envoy v1.38.5-dev が使用されます。アップグレードに関する具体的な手順は、提供されたリンク先のドキュメントを参照してください。
影響有無: 既存のサービスへの直接的な影響はありません。これは新バージョンの利用可能化に関するアナウンスであり、既存環境の動作を自動的に変更するものではありません。しかし、後述の通りセキュリティ修正が含まれるため、セキュリティ強化の観点からアップグレードを推奨します。
対処方法: Cloud Service Mesh をご利用中の場合、最新のセキュリティ修正と機能改善を適用するため、このバージョンへのアップグレードを検討することを推奨します。アップグレード作業は運用中のサービスに影響を与える可能性があるため、事前にテスト環境で十分な検証を実施してください。
用語説明:
*   **In-cluster Cloud Service Mesh**: Google Kubernetes Engine (GKE) クラスター内にコントロールプレーンとデータプレーンをデプロイして運用する Cloud Service Mesh のデプロイメントモデル。コントロールプレーンの管理をユーザー自身が行います。
*   **Envoy**: Cloud Service Mesh のデータプレーンとして機能する、高性能なオープンソースのエッジ/サービスプロキシです。マイクロサービス間のトラフィックルーティング、負荷分散、監視などを担当します。

## Fixed

### Patch 1.30.4-asm.14 contains the fix for the following platform CVEs:
原文: `Patch 1.30.4-asm.14 contains the fix for the following platform CVEs: ... (CVE Table) ...`
説明: このパッチバージョン 1.30.4-asm.14 には、多数のプラットフォーム共通脆弱性識別子 (CVE) に対する修正が含まれています。これには、CVSSスコアが8.7 (High) のCVE-2026-84304、CVE-2026-84445 や、CVSSスコアが9.8 (Critical相当) のCVE-2022-31045 など、高い深刻度の脆弱性修正が含まれています。これらの脆弱性は、プロキシ、コントロールプレーン、Distrolessイメージ、CNIコンポーネントなど、Cloud Service Meshの様々なコンポーネントに影響を与える可能性があります。
影響有無: Cloud Service Mesh を利用している場合、これらのセキュリティ脆弱性が修正されることで、サービスのセキュリティ体制が大幅に向上します。脆弱性が悪用されるリスクが低減されるため、セキュリティの観点からは積極的なアップグレードが強く推奨されます。現在のバージョンにこれらの脆弱性が存在する場合、潜在的なセキュリティリスクを抱えていることになります。
対処方法: セキュリティリスクを軽減し、サービスの堅牢性を確保するため、速やかにCloud Service Meshをこのバージョン (1.30.4-asm.14) へアップグレードすることを強く推奨します。アップグレード手順については、提供されたドキュメント([Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade))を参照し、本番環境適用前に十分なテストを実施してください。
用語説明:
*   **CVE (Common Vulnerabilities and Exposures)**: 広く認知されている情報セキュリティ脆弱性および露出に対して、共通の識別子を付与するシステムです。これにより、脆弱性情報の共有と管理が容易になります。
*   **Severity**: 脆弱性の深刻度を示す指標で、通常はCommon Vulnerability Scoring System (CVSS) スコアに基づいて評価されます。スコアが高いほど深刻度が高いことを意味し、一般的にCVSSスコア 9.0-10.0はCritical、7.0-8.9はHighに分類されます。リリースノートに「Medium (9.8)」と記載されているCVE-2022-31045は、CVSSスコアから見て一般的にはCriticalに分類される深刻な脆弱性です。
*   **Proxy**: Cloud Service Mesh におけるデータプレーンの一部で、マイクロサービス間でやり取りされるネットワークトラフィックを傍受し、ポリシーの適用、メトリクスの収集、トラフィック制御などを実行するコンポーネント（主にEnvoy）。
*   **Control Plane**: Cloud Service Mesh の管理層で、サービスメッシュ全体の構成、ポリシー、証明書などを管理し、データプレーンのプロキシに適用します。
*   **Distroless**: 非常に小さなOSレスのコンテナイメージで、アプリケーションの実行に必要な最小限のライブラリと依存関係のみを含みます。これにより、攻撃対象領域を減らし、セキュリティを向上させます。
*   **CNI (Container Network Interface)**: コンテナランタイムがLinuxコンテナのネットワークインターフェースを設定するためのプラグインベースの仕様。Kubernetesなどのコンテナオーケストレーションシステムで利用されます。

---

## Announcement

### 1.29.7-asm.18 is now available for in-cluster Cloud Service Mesh.
原文: `1.29.7-asm.18 is now available for in-cluster Cloud Service Mesh. For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.29.7-asm.18 uses Envoy v1.37.6.`
説明: Cloud Service Mesh (ASM) のバージョン 1.29.7-asm.18 が、インクラスターデプロイメント向けにリリースされました。このバージョンでは、Envoy プロキシが v1.37.6 を使用します。アップグレードに関する詳細は提供されたドキュメントを参照してください。
影響有無: 既存のサービスへの直接的な影響はありません。これは新バージョンの利用可能化に関するアナウンスです。後述の通りセキュリティ修正が含まれるため、セキュリティ対策の観点からはアップグレードを推奨します。
対処方法: Cloud Service Mesh をご利用中の場合、最新のセキュリティ修正と機能改善を適用するため、このバージョンへのアップグレードを検討することを推奨します。アップグレード前にテスト環境での十分な検証を実施してください。

## Fixed

### Patch 1.29.7-asm.18 contains the fix for the following platform CVEs:
原文: `Patch 1.29.7-asm.18 contains the fix for the following platform CVEs: ... (CVE Table) ...`
説明: このパッチバージョン 1.29.7-asm.18 には、多数のプラットフォーム共通脆弱性識別子 (CVE) に対する修正が含まれています。これには、CVSSスコアが9.8 (Critical相当) のCVE-2022-31045 や、CVSSスコアが8.7 (High) のCVE-2026-84304、CVE-2026-84445 など、高い深刻度の脆弱性修正が含まれています。これらの脆弱性は、コントロールプレーン、Distrolessイメージ、CNIコンポーネントなど、Cloud Service Meshの様々なコンポーネントに影響を与える可能性があります。
影響有無: Cloud Service Mesh を利用している場合、これらのセキュリティ脆弱性が修正されることで、サービスのセキュリティ体制が向上します。脆弱性が悪用されるリスクが低減されるため、セキュリティの観点からは積極的なアップグレードが推奨されます。現在のバージョンにこれらの脆弱性が存在する場合、潜在的なセキュリティリスクを抱えていることになります。
対処方法: セキュリティリスクを軽減するため、速やかにCloud Service Meshをこのバージョン (1.29.7-asm.18) へアップグレードすることを強く推奨します。アップグレード手順については、提供されたドキュメント([Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade))を参照し、本番環境適用前に十分なテストを実施してください。

---

## Announcement

### 1.28.10-asm.40 is now available for in-cluster Cloud Service Mesh.
原文: `1.28.10-asm.40 is now available for in-cluster Cloud Service Mesh. For details on upgrading Cloud Service Mesh, see Upgrade Cloud Service Mesh. Cloud Service Mesh 1.28.10-asm.40 uses Envoy v1.36.10-dev.`
説明: Cloud Service Mesh (ASM) のバージョン 1.28.10-asm.40 が、インクラスターデプロイメント向けにリリースされました。このバージョンでは、Envoy プロキシが v1.36.10-dev を使用します。アップグレードに関する詳細は提供されたドキュメントを参照してください。
影響有無: 既存のサービスへの直接的な影響はありません。これは新バージョンの利用可能化に関するアナウンスです。後述の通りセキュリティ修正が含まれるため、セキュリティ対策の観点からはアップグレードを推奨します。
対処方法: Cloud Service Mesh をご利用中の場合、最新のセキュリティ修正と機能改善を適用するため、このバージョンへのアップグレードを検討することを推奨します。アップグレード前にテスト環境での十分な検証を実施してください。

## Fixed

### Patch 1.28.10-asm.40 contains the fix for the following platform CVEs:
原文: `Patch 1.28.10-asm.40 contains the fix for the following platform CVEs: ... (CVE Table) ...`
説明: このパッチバージョン 1.28.10-asm.40 には、多数のプラットフォーム共通脆弱性識別子 (CVE) に対する修正が含まれています。これには、CVSSスコアが9.8 (Critical相当) のCVE-2022-31045 や、CVSSスコアが8.7 (High) のCVE-2026-84304、CVE-2026-84445 など、高い深刻度の脆弱性修正が含まれています。これらの脆弱性は、プロキシ、コントロールプレーン、Distrolessイメージ、CNIコンポーネントなど、Cloud Service Meshの様々なコンポーネントに影響を与える可能性があります。
影響有無: Cloud Service Mesh を利用している場合、これらのセキュリティ脆弱性が修正されることで、サービスのセキュリティ体制が向上します。脆弱性が悪用されるリスクが低減されるため、セキュリティの観点からは積極的なアップグレードが推奨されます。現在のバージョンにこれらの脆弱性が存在する場合、潜在的なセキュリティリスクを抱えていることになります。
対処方法: セキュリティリスクを軽減するため、速やかにCloud Service Meshをこのバージョン (1.28.10-asm.40) へアップグレードすることを強く推奨します。アップグレード手順については、提供されたドキュメント([Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade))を参照し、本番環境適用前に十分なテストを実施してください。

---

**補足事項:**
お客様の環境でGoogle Cloud Composer2 (Compoer version 2.7.1、Airflow version 2.7.3) をご利用とのことですが、Cloud Composer は直接 Cloud Service Mesh を利用するサービスではありません。Cloud Service Mesh は、Google Kubernetes Engine (GKE) クラスターに別途導入するサービスメッシュ製品です。したがって、お客様の GKE クラスターに Cloud Service Mesh が導入されていない場合は、今回のリリースノートは直接的な影響を持ちません。

しかし、もしお客様の GKE クラスターに Cloud Service Mesh が構築・運用されている場合は、上記のセキュリティ修正は重要です。各バージョンに含まれる CVE 修正はセキュリティ対策上不可欠ですので、現在ご利用の Cloud Service Mesh のバージョンを確認し、必要に応じて最新のパッチバージョンへのアップグレード計画を立てることを強くお勧めします。
# Title: September 22, 2026 
Link: https://docs.cloud.google.com/release-notes#September_22_2026<br>
ご担当者様

Google Cloud のリリースノートに基づき、構築済みのサービスへの影響について調査いたしました。
特に、貴社でご利用中の Google Cloud Composer2 (Composer version 2.7.1、Airflow version 2.7.3) を念頭に置いて分析しています。

---

# Cloud SDK
## Breaking
原文: (記載なし)
説明：Cloud SDKに関するBreaking Changeのアナウンスですが、具体的な変更内容がリリースノートに記載されていません。通常、Breaking Changeは既存のワークフローやスクリプトに互換性のない変更をもたらす可能性があります。
影響有無：現状の情報だけでは影響有無は判断できません。もし Cloud SDK を利用した自動化スクリプトやCI/CDパイプラインなどを運用している場合、リリースノート本体で詳細を確認する必要があります。Composerの利用自体には直接影響しませんが、Composerのデプロイや管理、またはComposerのワークフローから `gcloud` CLIを利用しているケースで影響が出る可能性があります。
対処方法：Google Cloud SDKの公式リリースノートを参照し、詳細な変更内容を確認してください。特に、`gcloud` CLIのバージョンアップやAPIクライアントライブラリの利用に影響が出る可能性があります。
用語説明：
*   **Cloud SDK**: Google Cloud のリソースを管理するためのコマンドラインツール (gcloud CLI)、ライブラリ、およびその他のツールセットの集合体です。
*   **Breaking Change**: 既存のコードや設定、運用手順との互換性を損なう変更のこと。通常、バージョンアップ時に手動での修正や対応が必要になります。

---

# Compute Engine
## Deprecated
原文: As of September 15, 2026, NVIDIA P100 (`nvidia-tesla-p100` and `nvidia-tesla-p100-vws`) GPUs have reached end of support (EOS) and are shut down. You can no longer create, launch, or access Compute Engine instances or other Google Cloud resources that use NVIDIA P100 GPUs. For information about migrating your workloads to supported GPU alternatives such as the G2 (NVIDIA L4) or G4 (NVIDIA RTX PRO 6000) machine series, see NVIDIA P100 end of support. [NVIDIA P100 end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos)
説明：NVIDIA P100 GPU (`nvidia-tesla-p100` および `nvidia-tesla-p100-vws`) は、2026年9月15日をもってサポート終了 (EOS) となり、すでにシャットダウンされています。この日以降、P100 GPUを使用するCompute Engineインスタンスや他のGoogle Cloudリソースは作成、起動、アクセスできません。ワークロードをG2 (NVIDIA L4) やG4 (NVIDIA RTX PRO 6000) などのサポートされている代替GPUシリーズへ移行するよう促されています。
影響有無：
*   **既存のCompute Engineインスタンス**: 該当するP100 GPUを利用しているCompute Engineインスタンスは、すでに2026年9月15日以降停止しています。もし現在P100 GPUを利用しているインスタンスが稼働している場合、それはすでに停止しているか、P100 GPUを利用していないかのいずれかです。
*   **新規構築**: P100 GPUを利用した新規インスタンスの作成はできません。
*   **Google Cloud Composer2**: Composerはマネージドサービスであり、Compute EngineインスタンスのGPUを直接管理するものではないため、Composer自体には直接的な影響はありません。ただし、Composerのワークロードが外部のCompute Engineインスタンス（P100 GPUを利用）と連携している場合は、その連携がすでに停止している可能性があります。
対処方法：
*   現在P100 GPUを利用している、または過去に利用していたCompute Engineインスタンスがある場合、速やかにワークロードをNVIDIA L4 (G2) または NVIDIA RTX PRO 6000 (G4) など、Google Cloudがサポートする他のGPUタイプへ移行済みであることを確認してください。
*   具体的な移行手順は、提供されているドキュメント「[NVIDIA P100 end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos)」を参照してください。
用語説明：
*   **NVIDIA P100 GPU**: NVIDIA社製のPascalアーキテクチャに基づく高性能GPUで、主に機械学習、HPCなどの計算負荷の高いワークロードに利用されていました。
*   **EOS (End of Support)**: 製品やサービスのサポートが終了すること。通常、EOS後はベンダーからのパッチ提供や技術サポートが受けられなくなり、機能の停止やセキュリティリスクが増大します。
*   **Compute Engine**: Google Cloud が提供する、仮想マシン (VM) を実行するためのサービス。

---

## Deprecated
原文: NVIDIA T4 (`nvidia-tesla-t4` and `nvidia-tesla-t4-vws`) and NVIDIA P4 (`nvidia-tesla-p4` and `nvidia-tesla-p4-vws`) GPUs are deprecated and will reach end of support (EOS) on August 1, 2027. After August 1, 2027, you won't be able to create, launch, or access Compute Engine instances or other Google Cloud resources that run NVIDIA T4 or P4 GPUs. In addition, you can no longer purchase or renew 3-year committed use discounts (CUDs) for NVIDIA T4 or P4 GPUs. To transition your workloads to supported GPU models such as the G2 (NVIDIA L4) or G4 (NVIDIA RTX PRO 6000) machine series before the EOS date, see NVIDIA T4 end of support and NVIDIA P4 end of support. [NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos) [NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos)
説明：NVIDIA T4 GPU (`nvidia-tesla-t4` および `nvidia-tesla-t4-vws`) と NVIDIA P4 GPU (`nvidia-tesla-p4` および `nvidia-tesla-p4-vws`) が非推奨となり、2027年8月1日にサポート終了 (EOS) となります。この日以降、T4またはP4 GPUを使用するCompute Engineインスタンスや他のGoogle Cloudリソースは作成、起動、アクセスできなくなります。また、T4またはP4 GPUに対する3年間のコミット済み使用割引 (CUD) の購入や更新はできなくなっています。ワークロードをEOS日までにG2 (NVIDIA L4) やG4 (NVIDIA RTX PRO 6000) などのサポートされているGPUモデルへ移行することが推奨されています。
影響有無：
*   **既存のCompute Engineインスタンス**: 現在NVIDIA T4またはP4 GPUを利用しているCompute Engineインスタンスは、2027年8月1日以降シャットダウンされ、アクセスできなくなります。
*   **新規構築**: EOS日までは作成可能ですが、長期的な利用は推奨されません。
*   **コミット済み使用割引 (CUD)**: T4/P4 GPUに対する新規の3年CUDの購入や既存CUDの更新はできません。これにより、コスト効率が低下する可能性があります。
*   **Google Cloud Composer2**: Composer自体には直接的な影響はありません。ただし、Composerのワークロードが外部のCompute Engineインスタンス（T4/P4 GPUを利用）と連携している場合は、EOS日以降、その連携が停止します。
対処方法：
*   現在NVIDIA T4またはP4 GPUを利用しているCompute Engineインスタンスがある場合、2027年8月1日のEOS日までにワークロードをNVIDIA L4 (G2) または NVIDIA RTX PRO 6000 (G4) など、Google Cloudがサポートする他のGPUタイプへ移行する計画を立ててください。
*   3年CUDを利用している場合、契約期間とEOS日を照らし合わせ、代替GPUへの移行計画にCUDの終了時期を考慮に入れてください。
*   具体的な移行手順は、提供されているドキュメント「[NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos)」および「[NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos)」を参照してください。
用語説明：
*   **NVIDIA T4/P4 GPU**: T4はTuringアーキテクチャ、P4はPascalアーキテクチャに基づくGPUで、P100と同様に機械学習推論やグラフィック処理などに広く利用されていました。
*   **Deprecated (非推奨)**: 将来的にサポートが終了したり、代替機能に置き換えられたりする予定の機能や製品。継続利用は可能ですが、新規利用は推奨されず、移行計画を立てることが求められます。
*   **CUD (Committed Use Discounts)**: Google Cloud のリソースを一定期間 (1年または3年) コミットして利用することで得られる大幅な割引。

---

ご不明な点がございましたら、お気軽にお問い合わせください。
# Title: September 21, 2026 
Link: https://docs.cloud.google.com/release-notes#September_21_2026<br>
Google Cloudのリリースノートを元に、構築済みのApigee Xサービスへの影響を調査し、以下に簡潔にまとめました。

---

# Apigee X
## Announcement
原文: On September 21st, 2026, we began maintenance updates of Apigee instances configured for maintenance windows.
[configured for maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows)
If you set a preferred window for maintenance for your instance, and your instance version is
below **1-18-0-apigee-4**, your instance will be updated to **1-18-0-apigee-4** within the
next seven to 21 days. A notification containing the expected date of upgrade will be sent within the next two business days.

Note: Instances that meet either of the following two criteria will not be updated:

- Your instance has a DNS misconfiguration, as described in Known Issue 445936920.
- Your instance uses an Apigee Java Library that has been removed, as described in Apigee release notes dated October 16, 2025.

[Known Issue 445936920](https://docs.cloud.google.com/apigee/docs/release/known-issues)
[Apigee release notes dated October 16, 2025](https://docs.cloud.google.com/apigee/docs/release/release-notes#October_16_2025)
For more information on participating in scheduled maintenance windows, see Maintenance overview and Manage Apigee instance maintenance windows.

[Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance)
[Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows)

説明：
2026年9月21日より、メンテナンスウィンドウが設定されているApigeeインスタンスのメンテナンスアップデートが開始されました。
もし、Apigeeインスタンスに推奨されるメンテナンスウィンドウを設定しており、かつ現在のバージョンが **1-18-0-apigee-4** 未満の場合、お使いのインスタンスは今後7〜21日以内に **1-18-0-apigee-4** へとアップデートされます。アップグレード予定日を含む通知が2営業日以内に送信される予定です。
ただし、以下のいずれかの条件に合致するインスタンスはアップデートされません。
*   既知の問題 445936920 に記載されているようなDNS設定の誤りがあるインスタンス。
*   2025年10月16日付のApigeeリリースノートに記載されている、削除されたApigee Java Libraryを使用しているインスタンス。

影響有無：
**影響あり。**
メンテナンスウィンドウを設定しているApigee Xインスタンスをご利用中で、かつ現在のインスタンスバージョンが `1-18-0-apigee-4` 未満の場合、自動的にアップデートが適用されます。これにより、新しい機能や修正が導入される一方で、互換性や動作確認が必要になる可能性があります。また、DNS設定不備や削除されたJava Libraryを使用している場合はアップデートがスキップされるため、その状態を把握し対処が必要か確認すべきです。

対処方法：
1.  **Apigeeインスタンスのバージョン確認**: 現在のApigeeインスタンスのバージョンを確認してください。
2.  **通知の確認**: メンテナンスウィンドウを設定している場合、Google Cloudから送信されるアップグレード予定日に関する通知を注意深く確認してください。
3.  **互換性検証**: 予定されるメンテナンス期間中に、Apigeeで稼働しているAPIやアプリケーションに影響がないか、事前にテスト環境で互換性検証を行うことを強く推奨します。
4.  **未アップデートインスタンスの確認**: インスタンスがDNS設定不備や削除されたApigee Java Libraryを使用しているためにアップデートがスキップされた場合は、これらの問題を修正し、必要に応じて手動でのアップデートを検討するか、Google Cloudサポートに相談してください。

用語説明：
*   **Apigee インスタンス**: Google CloudのApigee API Management Platformのデプロイ単位。APIプロキシ、セキュリティポリシー、開発者アプリケーションなどをホストします。
*   **メンテナンスウィンドウ (Maintenance Window)**: クラウドサービスプロバイダがシステムのメンテナンス作業（パッチ適用、アップグレードなど）を実施するために顧客と合意した時間帯。これにより、サービスへの影響を最小限に抑えられます。
*   **DNS misconfiguration (DNS設定不備)**: ドメインネームシステムの設定が誤っている状態。これにより、サービスが正しいIPアドレスに解決されず、接続や機能に問題が発生する可能性があります。
*   **Apigee Java Library**: Apigeeのカスタムポリシーなどで利用できるJava言語のライブラリ。特定バージョンで非推奨または削除されたものがあります。

---

## Announcement
原文: On September 21st, 2026, we released an updated version of Apigee (1-18-0-apigee-5).
> **Note:** Rollouts of this release began today and can take four or more business days to be completed across all Google Cloud zones. Your instances might not have the features and fixes available until the rollout is complete.

説明：
2026年9月21日に、Apigeeの更新バージョン `1-18-0-apigee-5` がリリースされました。このリリースは、すべてのGoogle Cloudゾーンに展開されるまでに4営業日以上かかる可能性があり、展開が完了するまでは新機能や修正が利用できない場合があります。

影響有無：
**影響あり。**
新しいバージョンがリリースされたことで、今後のメンテナンスでこのバージョンが自動的に適用される可能性があります。これにより、新機能や修正が利用可能になります。ただし、ロールアウトに時間がかかるため、すべてのゾーンで即座に機能が利用できるわけではない点に留意が必要です。

対処方法：
特別な対処は通常不要です。Apigeeインスタンスが新しいバージョンに更新された後、新機能の有無や既存機能の動作に問題がないか、継続的に監視してください。緊急でこのバージョンの特定の機能や修正が必要な場合は、Google Cloudゾーンでの展開状況を考慮し、展開完了後に利用可能になることを理解しておく必要があります。

用語説明：
*   **ロールアウト (Rollout)**: ソフトウェアの新しいバージョンや機能が、段階的または順次的にユーザーやシステムに展開されていくプロセス。

---

## Security
原文:
| Bug ID | Description |
| --- | --- |
| **560130499** | **Security fix for Apigee.** Fixed a security issue in the Java Callout policy. |
| **547681234** | **Security fix for Apigee.** Patched CVE-2026-69247 by upgrading a third-party library used by the Apigee model-security engine. |
| **556568593** | **Security fix for Apigee.** Patched CVE-2026-84304 by upgrading gRPC. |
| **N/A** | **Security fix for Apigee infrastructure.** |
[CVE-2026-69247](https://nvd.nist.gov/vuln/detail/CVE-2026-69247)
[CVE-2026-84304](https://nvd.nist.gov/vuln/detail/CVE-2026-84304)

説明：
複数のセキュリティ修正が適用されました。具体的には、Java Calloutポリシーにおけるセキュリティ問題の修正、Apigeeモデルセキュリティエンジンで使用されるサードパーティライブラリのアップグレードによるCVE-2026-69247のパッチ適用、gRPCのアップグレードによるCVE-2026-84304のパッチ適用、およびApigeeインフラストラクチャのセキュリティ修正が含まれます。

影響有無：
**影響あり（ポジティブな影響）。**
これらのセキュリティ修正により、Apigee環境のセキュリティ体制が強化され、既知の脆弱性（CVE）が解消されるため、サービスのリスクが軽減されます。ユーザー側で直接的な対応は通常不要ですが、サービスがより安全になります。

対処方法：
これらのセキュリティ修正は、Apigeeのバージョンアップグレードを通じて自動的に適用されます。ユーザー側で直接的な対処は不要ですが、Apigeeのメンテナンスウィンドウ設定やバージョン管理を通じて、最新のセキュリティパッチが適用されていることを確認することが重要です。

用語説明：
*   **Java Callout policy (Javaコールアウトポリシー)**: Apigee APIプロキシのフロー内でカスタムJavaコードを実行できるポリシー。標準ポリシーでは実現できない複雑なロジックの実装に利用されます。
*   **CVE (Common Vulnerabilities and Exposures)**: 既知のサイバーセキュリティの脆弱性や露出を一意に識別するための共通識別子システム。
*   **gRPC**: Googleによって開発された、高性能でオープンソースなリモートプロシージャコール (RPC) フレームワーク。

---

## Fixed
原文:
| Bug ID | Description |
| --- | --- |
| **559009293** | Fixed elevated OAuth and VerifyAPIKey latency and Cassandra read load for AppGroup apps by caching the AppGroup entity in the Message Processor runtime, matching Developer-app behavior. |
| **558888960** | Fixed distributed tracing so that the target URL is included as a span attribute in all scenarios. |
| **556750755** | Fixed EventFlow (Server-Sent Events) dropping or truncating events that follow a large (greater than 16 KB) event under load on the http-adaptor data path. |
| **553931019** | The MCP tools/list method now aggregates tools across all approved API products. |
| **531783017** | Implemented the `<Enforce>true</Enforce>` element of SSLInfo for a Syslog endpoint, so that the syslog target's TLS server identity is verified. |
| **554114419** | Policies can now change request pseudo-headers (for example, :path and :authority) when HTTP/2 is in use. |
| **548763108** | Blocked outbound HTTP from the Message Processor to Kubernetes-internal targets. |
| **513032450** | Restored a 15-second TCP keep-alive on the Apigee Connect control-plane connection so that a silently dropped connection recovers in seconds rather than approximately two hours. |
| **N/A** | Updates to infrastructure and libraries. |

説明：
複数の不具合が修正されました。主な修正点は以下の通りです。
*   AppGroupアプリにおけるOAuthおよびVerifyAPIKeyのレイテンシ増加とCassandra読み込み負荷が、Message ProcessorランタイムでのAppGroupエンティティキャッシュにより改善され、Developer-appと同等の動作になりました。
*   分散トレースにおいて、ターゲットURLがすべてのシナリオでスパン属性として含まれるようになりました。
*   EventFlow (Server-Sent Events) で、http-adaptorデータパスにおいて、16KBを超える大きなイベントの後に続くイベントが負荷時にドロップまたは切り捨てられる問題が修正されました。
*   MCP tools/list メソッドが、承認されたすべてのAPIプロダクト間でツールを集計するようになりました。
*   SyslogエンドポイントのSSLInfoに`<Enforce>true</Enforce>`要素が実装され、syslogターゲットのTLSサーバーIDが検証されるようになりました。
*   HTTP/2使用時、ポリシーがリクエストの擬似ヘッダー（例: `:path`、`:authority`）を変更できるようになりました。
*   Message ProcessorからKubernetes内部ターゲットへのアウトバウンドHTTPがブロックされました。
*   Apigee Connectコントロールプレーン接続において15秒のTCPキープアライブが復元され、サイレントに切断された接続が約2時間ではなく数秒で回復するようになりました。
*   インフラストラクチャとライブラリが更新されました。

影響有無：
**影響あり（ポジティブな影響）。**
既存のいくつかの問題やパフォーマンス、機能の不具合が修正されるため、システムの安定性、信頼性、パフォーマンス、セキュリティが向上します。特に、AppGroupアプリ利用時のレイテンシ改善、分散トレースの精度向上、EventFlowの安定性向上、Apigee Connect接続の回復性向上などは、既存のワークロードにプラスの影響を与える可能性があります。Message ProcessorからKubernetes内部ターゲットへのアウトバウンドHTTPがブロックされた点は、通常セキュリティ強化のためですが、もし意図的にそのような通信に依存していた場合は、影響を再評価する必要があります。

対処方法：
これらの修正は、Apigeeのバージョンアップグレードを通じて自動的に適用されるため、ユーザー側の直接的な対処は通常不要です。
もし、AppGroupアプリのレイテンシ問題、EventFlowのイベント損失、分散トレース情報の不足、HTTP/2のポリシー制約、Apigee Connectの接続安定性といった問題に直面していた場合は、これらの修正が適用されることで問題が解消されるか確認し、その恩恵を享受できます。

用語説明：
*   **OAuth**: 認証および認可のためのオープン標準プロトコル。APIアクセスを安全に委任するために広く使用されます。
*   **VerifyAPIKey policy (APIキー検証ポリシー)**: Apigeeのポリシーで、受信するAPIリクエストに有効なAPIキーが含まれているかを確認します。
*   **Cassandra**: 大規模な分散型NoSQLデータベース。Apigeeの内部データストアとして利用されます。
*   **AppGroup (App Group)**: Apigeeの機能で、複数の開発者アプリケーションを論理的にグループ化し、共通のアクセス制御や設定を適用するためのものです。
*   **Message Processor (メッセージプロセッサ)**: Apigeeランタイム環境の主要コンポーネントの一つで、APIリクエストの処理、ポリシーの実行、バックエンドへのルーティングを行います。
*   **Distributed Tracing (分散トレース)**: マイクロサービスアーキテクチャのような分散システムにおいて、単一のリクエストが複数のサービスをまたいでどのように流れるかを追跡するための技術。
*   **Span (スパン)**: 分散トレースにおける作業の論理的な単位。通常、単一の操作やサービス呼び出しを表します。
*   **EventFlow (Server-Sent Events)**: サーバーからクライアントへ一方的にデータをプッシュするWeb技術（Server-Sent Events、SSEのApigeeでの実装名）。リアルタイム通知などに使用されます。
*   **Syslog endpoint**: システムログメッセージを収集、転送、保存するためのターゲット。
*   **TLS server identity verification (TLSサーバーID検証)**: クライアントがTLS証明書を検証し、接続先のサーバーが主張する通りの正当なサーバーであることを確認するセキュリティプロセス。
*   **Pseudo-headers (擬似ヘッダー)**: HTTP/2などのプロトコルで使用される特殊なヘッダーで、コロン（:）で始まり、HTTP/1.1のステータスラインやリクエストラインの情報を表します（例: `:path`, `:authority`）。
*   **Kubernetes-internal targets (Kubernetes内部ターゲット)**: Kubernetesクラスタ内で実行されているサービスやPodの内部ネットワークアドレス。
*   **Apigee Connect**: Apigeeと顧客のオンプレミス環境や他のクラウド環境との間でセキュアな接続を確立するためのコンポーネント。
*   **TCP keep-alive**: TCP接続が確立された後、一定時間データが流れていない場合に、接続がアクティブであることを確認するために小さなパケットを送信するメカニズム。これにより、ネットワーク機器による接続の切断を防ぎ、切断された場合に速やかに検出・回復できます。

---