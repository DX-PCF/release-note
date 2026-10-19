
# Title: October 16, 2026 
Link: https://docs.cloud.google.com/release-notes#October_16_2026<br>
はい、承知いたしました。Google Kubernetes Engineのリリースノートについて、製品への影響有無、対処方法を含めて調査結果を回答いたします。

---

# Google Kubernetes Engine

## Change

原文:
For GKE Standard CPU node pools, GKE can now upgrade nodes by updating the existing
Compute Engine VM in place, instead of deleting the VM and creating a new one.
Because the node keeps its underlying VM, it also keeps its compute capacity
during the upgrade. This lowers the risk that a node upgrade fails or stalls
because resources aren't available.

To enable this type of upgrade, use
surge upgrades with the `maxUnavailable` field
set to a value greater than 0. For more details about when GKE reuses the same
Compute Engine instance, including exceptions, see
maxUnavailable: GKE makes an existing node unavailable to recreate it.

This change applies to all GKE versions. To opt out, contact Cloud Customer Care.

説明：
GKE StandardのCPUノードプールにおいて、ノードのアップグレード方法が改善されました。これまでは、アップグレード時に既存のCompute Engine VMを削除し、新しいVMを再作成していましたが、今回の変更により、既存のCompute Engine VMをその場で（in-place）更新する方式が可能になりました。

これにより、ノードが基盤となるVMを保持したままアップグレードされるため、アップグレード中もコンピュートキャパシティを維持できます。結果として、リソース不足が原因でノードのアップグレードが失敗したり、停止したりするリスクが低減されます。

この新しいアップグレード方式を有効にするには、サージアップグレード（surge upgrades）を使用し、`maxUnavailable`フィールドの値を0より大きく設定する必要があります。この変更はすべてのGKEバージョンに適用されます。この挙動を希望しない場合は、Cloud Customer Careに連絡することでオプトアウトできます。

影響有無：
**影響なし（ただし、安定性向上の恩恵あり）**
この変更は、GKEのノードアップグレードの内部的な動作改善であり、既存のクラスタやワークロードに対する直接的な非互換性（Breaking Change）はありません。むしろ、アップグレードの安定性が向上し、リソース不足によるアップグレード失敗のリスクが低減されるため、運用面でのメリットがあります。

対処方法：
**特に対処は不要**です。
しかし、この安定性向上の恩恵を最大限に受けるためには、GKEのノードプールアップグレード戦略として、`maxUnavailable`が0より大きい値に設定されたサージアップグレードの使用を推奨します。これにより、アップグレード時のコンピュートキャパシティ維持と、リソース不足によるアップグレード失敗のリスク低減効果が得られます。

既存のアップグレード戦略がサージアップグレードではない場合や、`maxUnavailable=0`（ブルー/グリーンアップグレードやローリングアップグレードの一種）を使用している場合は、この改善の直接的な恩恵は受けられません。アップグレードの安定性や継続性を重視する場合は、サージアップグレード戦略への移行を検討する価値があります。

用語説明：
*   **GKE Standard CPU node pools**: Google Kubernetes Engineの標準クラスタにおいて、CPUリソースを基盤とするノード群（ノードプール）を指します。
*   **in-place upgrade**: 新しいリソースをプロビジョニングするのではなく、既存のリソースを直接更新するアップグレード手法です。これにより、リソースの再作成に伴う一時的なリソース消費やキャパシティ変動を避けることができます。
*   **surge upgrades (サージアップグレード)**: GKEのノードプールアップグレード戦略の一つで、既存のノードをシャットダウンする前に、一時的に追加のノードをプロビジョニングしてワークロードを移動させる方式です。これにより、アップグレード中のダウンタイムを最小限に抑えることができます。
*   **`maxUnavailable`**: GKEのノードプールアップグレード時に、同時に利用不可にできるノードの最大数または最大割合を指定するパラメータです。この値が0より大きい場合、GKEはアップグレード中に一時的にノード数を増やす（サージ）ことで、利用可能なノード数を維持しようとします。
*   **Cloud Customer Care**: Google Cloudの公式サポート窓口です。製品に関する問い合わせや問題解決のために利用します。
# Title: October 15, 2026 
Link: https://docs.cloud.google.com/release-notes#October_15_2026<br>
Google Cloud のリリースノートに基づき、構築済みのサービスへの影響調査結果を以下に報告いたします。

---

# Apigee X
## Fixed
原文:
```
| Bug ID | Description |
| --- | --- |
| **466116259** | Updated the startup script for the managed instance group (MIG) that routes external traffic to Apigee. `net.ipv4.ip_forward` is now written to `/etc/sysctl.d/`, so an instance no longer stops forwarding traffic when a reboot or an OS update resets it. The script does not change unrelated `iptables` NAT rules. Instances pick up the change the next time they are restarted or recreated. |
```
説明：
Apigee に外部トラフィックをルーティングするマネージドインスタンスグループ (MIG) の起動スクリプトが更新されました。これにより、`net.ipv4.ip_forward` の設定が `/etc/sysctl.d/` に永続的に書き込まれるようになります。この修正により、インスタンスの再起動やOSアップデートによってIPフォワーディングの設定がリセットされ、トラフィック転送が停止する問題が解消されます。このスクリプトの変更は、関連しない `iptables` の NAT ルールには影響を与えません。変更は、インスタンスが次に再起動または再作成された際に適用されます。

影響有無：
**影響なし（むしろ改善）**。
これは既存の Apigee X の運用におけるバグ修正であり、サービスがより安定して外部トラフィックを転送できるようになります。既存の構成に対する破壊的な変更や、追加の作業は必要ありません。インスタンスが再起動または再作成された際に自動的に修正が適用されます。

対処方法：
特段の対処は必要ありません。MIG のインスタンスが計画的な運用サイクルで再起動または再作成されるのを待つことで、自動的に修正が適用されます。緊急に修正を適用したい場合は、該当する MIG のインスタンスを意図的に再起動または再作成することで、即座に修正を反映させることが可能です。

用語説明：
*   **Apigee X**: Google Cloud が提供する API 管理プラットフォームの最新バージョン。API の設計、開発、セキュリティ、スケーリング、分析などを統合的に管理します。
*   **マネージドインスタンスグループ (MIG)**: Google Compute Engine の機能の一つで、同種の仮想マシン (VM) インスタンスのグループを管理し、オートスケーリング、自動修復、ロードバランシングなどの機能を提供します。
*   **`net.ipv4.ip_forward`**: Linux カーネルのネットワークパラメータの一つで、IP パケットの転送（フォワーディング）を有効にするかどうかを制御します。ルーターやゲートウェイとして機能するサーバーで有効にされることが多いです。
*   **`/etc/sysctl.d/`**: システムのランタイム設定を永続化するためのディレクトリ。このディレクトリ内の設定ファイルに記述された内容は、システムの再起動後も保持されます。
*   **`iptables`**: Linux システムで IP パケットのフィルタリング、NAT (Network Address Translation)、およびその他のパケット操作を設定するためのコマンドラインユーティリティです。

---

# Compute Engine
## Change
原文:
```
If you try to create an on-demand reservation or increase the number of
reserved Compute Engine instances in a reservation when the zone has
reached its reservation capacity limit for your requested machine family, then
the request fails with a `RESERVATION_CAPACITY_LIMIT_EXCEEDED` error. For more
information, see
Reservation capacity limit exceeded.

[Reservation capacity limit exceeded](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-creation#reservation-capacity-limit-exceeded)
```
説明：
オンデマンド予約の作成や、既存の予約で Compute Engine インスタンス数を増やそうとした際に、リクエストされたゾーンが要求されたマシンファミリーの予約容量制限に達している場合、リクエストが `RESERVATION_CAPACITY_LIMIT_EXCEEDED` エラーで失敗するようになりました。詳細については、提供されたトラブルシューティングドキュメントをご確認ください。

影響有無：
**影響あり**。
これは、Compute Engine のオンデマンド予約の挙動変更であり、特定の状況下で予約リクエストが失敗するようになることを意味します。これまで成功していた予約リクエストが、ゾーンのキャパシティ制限に達している場合にエラーとなる可能性があります。特に、重要なワークロードや本番環境で必要なリソースを確保するために予約に依存している場合、計画通りのリソース確保が困難になる可能性があります。

対処方法：
1.  **エラーハンドリングの強化**: 予約の作成や変更を行う自動化スクリプトやツールにおいて、`RESERVATION_CAPACITY_LIMIT_EXCEEDED` エラーを適切にハンドリングするロジックを実装してください。これには、エラー発生時の再試行、別のゾーンやリージョンでのリソース確保の検討、運用担当者への通知などが含まれます。
2.  **キャパシティプランニングの徹底**: 重要なワークロードやピーク時の需要を見越して、事前に十分な Compute Engine リソースのオンデマンド予約を確保するように計画してください。定期的にゾーンごとのキャパシティ状況を確認し、必要に応じて予約量を調整します。
3.  **代替オプションの検討**:
    *   特定のゾーンで予約が困難な場合、代替となる別のゾーンまたはリージョンへのデプロイを検討します。
    *   予約が困難なマシンファミリーがある場合、類似の性能を持つ別のマシンファミリーの利用を検討します。
    *   緊急時や一時的な利用には、スポット VM やプリエンプティブル VM の利用も代替手段として考慮できます（ただし、可用性は保証されません）。
4.  **Google Cloud サポートへの相談**: 大規模な予約が必要で、継続的にキャパシティ制限に直面する場合は、Google Cloud サポートに連絡し、キャパシティ確保の可能性や推奨事項について相談してください。

用語説明：
*   **オンデマンド予約 (On-demand Reservation)**: Google Compute Engine の機能の一つで、特定の Compute Engine リソース（VM インスタンスの vCPU、メモリなど）を事前に予約することで、必要なときにリソースが利用可能であることを保証するサービスです。これにより、キャパシティ不足によるインスタンス起動の失敗リスクを低減できます。
*   **マシンファミリー (Machine Family)**: Compute Engine における VM インスタンスのタイプ分類です。例えば、汎用 (N2D, E2)、計算集約型 (C2)、メモリ最適化型 (M2) などがあり、特定のワークロードに最適化されたハードウェア構成を提供します。
*   **ゾーン (Zone)**: Google Cloud リージョン内に存在する、物理的に独立したデータセンターの集合体です。単一ゾーン障害からの回復性を高めるため、通常は複数のゾーンにリソースを分散してデプロイすることが推奨されます。
*   **`RESERVATION_CAPACITY_LIMIT_EXCEEDED`**: Google Compute Engine において、要求されたゾーンの予約容量が、指定されたマシンファミリーに対してすでに上限に達している場合に返されるエラーコードです。