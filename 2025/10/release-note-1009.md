
# Title: October 07, 2025 
Link: https://cloud.google.com/release-notes#October_07_2025<br>
はい、承知いたしました。Google Cloudのリリースノートに基づき、各製品への影響と対処方法を調査し、以下の通りご回答いたします。

---

# Apigee X
## Breaking
原文: `Previously unreported customer DNS misconfigurations now result in DNS errors`
`Apigee removed the automatic DNS fallback functionality that was in 1-16-0-apigee-2. This removal surfaces customer DNS misconfigurations that previously did not show as DNS errors.`
`See Known Issue 445936920.`

説明:
Apigee Xのバージョン1-16-0-apigee-2に存在していた自動DNSフォールバック機能が削除されました。この変更により、これまで自動フォールバック機能によって隠蔽されていた顧客環境のDNS設定ミスが、DNSエラーとして顕在化するようになります。これは既存のサービス動作に影響を与える可能性のあるBreaking Changeです。

影響有無:
**影響あり**。
Apigee Xを利用している環境で、もし何らかのDNS設定ミス（カスタムドメインの設定不備、外部サービスのエンドポイント解決ミスなど）が存在していた場合、この変更によってこれまで問題なく動作していたAPIプロキシやサービス連携が、DNSエラーにより停止する可能性があります。特に、外部システムへの接続やカスタムドメインを利用しているAPIに関して、影響範囲の確認が必要です。

対処方法:
1.  **影響範囲の確認**: Apigee X環境におけるカスタムドメイン設定や、外部サービスへのアウトバウンド接続がDNS解決に依存している部分を特定します。
2.  **ログおよびモニタリングの確認**: Apigee Xのログ（Cloud Loggingなど）やAPIモニタリングツールを確認し、DNS関連のエラー（例: `DNS_RESOLUTION_FAILED`など）が増加していないか、または発生していないか監視を強化します。
3.  **DNS設定の正確性確認**: 影響が確認された場合、または予防的に、関連するDNSレコード（Aレコード、CNAMEレコードなど）が正確に設定されているかを確認し、必要に応じて修正します。
4.  **既知の問題の参照**: 提供されている[Known Issue 445936920](https://cloud.google.com/apigee/docs/release/known-issues#445936920) を参照し、詳細な情報や具体的な回避策がないか確認してください。

用語説明:
*   **DNSフォールバック機能**: DNS解決に失敗した場合に、自動的に代替のDNSサーバや設定（例: 公開DNS、セカンダリDNSサーバなど）を使用して解決を試みる機能です。これにより、一時的なDNS解決の失敗がエンドユーザーに影響を与えないようにできます。
*   **DNS設定ミス (DNS misconfigurations)**: ドメイン名とIPアドレスのマッピングを行うDNSレコード（例: Aレコード、CNAMEレコード）の設定が誤っている状態を指します。これにより、対象のサービスに正しくアクセスできない、通信が確立できないなどの問題が発生します。

---

# BigQuery
## Announcement
原文: `As of February 25, 2025, enhancements to the workload management autoscaler that were announced on July 31, 2024 have rolled out to all users. These enhancements are generally available (GA).`
`[workload management autoscaler](https://cloud.google.com/bigquery/docs/slots-autoscaling-intro)`
`[July 31, 2024](https://cloud.google.com/bigquery/docs/release-notes#July_31_2024)`
`[generally available](https://cloud.google.com/products#product-launch-stages)`

説明:
BigQueryのワークロード管理オートスケーラーに対する機能強化が、2025年2月25日をもって全ユーザーに適用され、一般提供（GA）となりました。この機能強化は、既に2024年7月31日に発表されていたものです。

影響有無:
**影響なし（ただしポジティブな影響の可能性あり）**。
これは既存機能の改善であり、ユーザーが明示的に設定変更を求められるものではありません。既存のBigQueryのワークロードに対して悪影響を及ぼす可能性は非常に低く、むしろワークロード管理オートスケーラーの賢さや効率性が向上することで、BigQueryのクエリパフォーマンスの改善やリソース利用の最適化といったポジティブな効果が期待されます。

対処方法:
**不要**。
この機能強化は自動的に適用されるため、ユーザー側で特別な対処は必要ありません。BigQueryのワークロード管理（スロットの予約やオートスケーリング）を積極的に利用している場合は、関連ドキュメントを参照し、強化された機能について理解を深めることで、今後の利用戦略に役立てることができます。

用語説明:
*   **ワークロード管理オートスケーラー (Workload Management Autoscaler)**: BigQueryにおいて、クエリ実行に必要な計算リソースである「スロット」の割り当てを、現在のワークロードの需要に応じて自動的に調整する機能です。これにより、ユーザーは手動でスロット数を増減させる手間が省け、リソースを効率的に利用し、コストを最適化できます。
*   **スロット (Slots)**: BigQueryでSQLクエリを実行するために使用される計算能力の抽象的な単位です。クエリの複雑さや処理するデータ量に応じて、必要なスロット数が変動します。
*   **一般提供 (Generally Available, GA)**: Google Cloudのサービスや機能が、プロダクション環境での利用が推奨される安定した状態に達したことを示すリリースステージです。GAに達した機能は、SLA（サービス品質保証）の対象となり、Google Cloudによる完全なサポートが提供されます。

---
# Title: October 06, 2025 
Link: https://cloud.google.com/release-notes#October_06_2025<br>
Google Cloudのリリースノートに関する影響調査の結果を以下にまとめます。

---

# BigQuery

## Announcement

**原文:**
Starting March 17, 2026, the BigQuery Data Transfer Service will require the
`bigquery.datasets.setIamPolicy` and the `bigquery.datasets.getIamPolicy`
permissions on the target dataset to create or update a transfer configuration.
For more information, see Changes to dataset-level access controls.

[Changes to dataset-level access controls](https://cloud.google.com/bigquery/docs/dataset-access-control)

**説明:**
2026年3月17日以降、BigQuery Data Transfer Service で転送設定を作成または更新する際に、転送先のデータセットに対して `bigquery.datasets.setIamPolicy` および `bigquery.datasets.getIamPolicy` のIAM権限が必要となります。これにより、データ転送のセキュリティ管理が強化されます。

**影響有無:**
**影響あり（将来的な対応が必要）**
現在 BigQuery Data Transfer Service を利用しており、転送設定の作成者または更新者がこれらの権限を持っていない場合、将来的に影響があります。特に、サービスアカウントやカスタムロールを使用して転送設定を管理している場合は、これらの権限が付与されているか確認が必要です。2026年3月17日という猶予期間があるため、直ちにサービスが停止することはありません。

**対処方法:**
BigQuery Data Transfer Service を利用している場合、2026年3月17日までに以下の対応を検討してください。
1.  BigQuery Data Transfer Service の転送設定を作成または更新するユーザー、またはサービスアカウントに対して、転送先データセットに対する `bigquery.datasets.setIamPolicy` と `bigquery.datasets.getIamPolicy` 権限が付与されていることを確認します。
2.  これらの権限は通常、`roles/bigquery.dataEditor` や `roles/bigquery.admin` などの事前定義ロールに含まれていますが、より詳細なカスタムロールを使用している場合は明示的に追加する必要があります。
3.  詳細については、提供されているリンク「Changes to dataset-level access controls」を参照し、IAMポリシーの見直しを計画してください。

**用語説明:**
*   **BigQuery Data Transfer Service:** Google BigQueryに対して、Google SaaSアプリケーション（Google Ads、Google Analyticsなど）や外部ソース（Amazon S3など）からデータを自動的かつ定期的に転送・ロードするサービスです。
*   **IAM (Identity and Access Management):** Google Cloudリソースへのアクセスをきめ細かく制御するためのフレームワークです。誰が（Principal）、どのリソースに対して（Resource）、どのような操作を（Role）できるかを定義します。
*   **`bigquery.datasets.setIamPolicy` / `bigquery.datasets.getIamPolicy`:** BigQueryデータセットのIAMポリシーを設定・取得するための権限です。これらの権限は、データセットのアクセス制御を変更する際に必要となります。

---

# Compute Engine

## Changed

**原文:**
The Google Cloud optimized (`-optimized-gcp`) and accelerated (`optimized-gcp-nvidia-*`) versions of the Rocky Linux images now include the CIQ SIG/Cloud Next repository. This repository provides a cloud-optimized kernel. Additionally, the accelerated images now also include the CIQ SIG/Cloud Next Nonfree repository, which provides access to proprietary GPU drivers for the cloud-optimized kernel.

[CIQ SIG/Cloud Next repository](https://docs.ciq.com/rlc/ciq-sig-cloud-next/)
[CIQ SIG/Cloud Next Nonfree repository](https://gitlab.com/ctrl-iq-public/sig-cloud-next/next-nonfree)
This update is applied to images created on or after September 12, 2025.

For more information about Rocky Linux OS images, see Rocky Linux on the operating system details page.

[Rocky Linux](https://cloud.google.com/compute/docs/images/os-details#rocky_linux)

**説明:**
Compute Engine で提供されるRocky LinuxのGoogle Cloud最適化バージョン（`-optimized-gcp`）およびアクセラレーテッドバージョン（`optimized-gcp-nvidia-*`）のイメージに、CIQ SIG/Cloud Nextリポジトリが追加されます。これにより、クラウド環境に最適化されたカーネルが提供されます。さらに、アクセラレーテッドイメージには、クラウド最適化カーネル用のプロプライエタリなGPUドライバーを提供するCIQ SIG/Cloud Next Nonfreeリポジトリも含まれるようになります。この変更は2025年9月12日以降に作成されるイメージに適用されます。

**影響有無:**
**影響なし（既存のサービスに直接的な影響はない）**
既存のCompute Engineインスタンスには直接的な影響はありません。この変更は、2025年9月12日以降に新しく作成されるRocky Linuxイメージに適用されるものです。将来的に新しいインスタンスを起動する際に、より最適化されたカーネルやGPUドライバーが含まれるイメージが利用可能になります。これにより、パフォーマンスの向上や特定のハードウェアサポートの改善が期待できます。

**対処方法:**
特別な対処は不要です。
*   現在稼働中のCompute Engineインスタンスは影響を受けません。
*   2025年9月12日以降にRocky Linuxの `-optimized-gcp` または `optimized-gcp-nvidia-*` イメージを使用して新しいインスタンスをデプロイする際、これらの新しいリポジトリが自動的に含まれたイメージが使用されることを認識しておけば十分です。
*   もし、特定のカーネルバージョンやドライバーに厳密に依存するアプリケーションを運用している場合は、新しいイメージで動作確認を行うことを検討しても良いでしょう。

**用語説明:**
*   **Rocky Linux:** オープンソースのLinuxディストリビューションで、Red Hat Enterprise Linux (RHEL) との互換性を持つことを目的としています。CentOSの後継として開発されました。
*   **Google Cloud optimized images:** Google Cloud環境での実行に特化して最適化されたOSイメージです。通常、パフォーマンス向上のためのチューニングや、必要なドライバ、ツールなどがプリインストールされています。
*   **CIQ SIG/Cloud Next repository:** CIQ社が提供する、クラウド環境（特にGoogle Cloud）向けに最適化されたカーネルや関連パッケージを提供するリポジトリです。これにより、仮想マシンでの性能や安定性が向上します。
*   **Cloud-optimized kernel:** クラウド環境（仮想マシンやコンテナなど）での動作に特化して最適化されたLinuxカーネルです。一般的なサーバーカーネルに比べて、仮想化環境での効率やパフォーマンスが向上するように設計されています。
*   **Proprietary GPU drivers:** 特定のGPUハードウェアメーカーによって開発・提供される、クローズドソース（非公開）のグラフィックスドライバーです。これらは通常、最高のパフォーマンスや機能を提供するために必要とされます。